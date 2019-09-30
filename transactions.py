from enum import Enum

from credit import Credit
from expense import Expense
from summary_printer import SummaryPrinter


class Transaction:

    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = float(amount)
        self.balance = float(balance)
        self.is_out = self.amount < 0
        self.type = Expense.from_description(self.description) if self.is_out else Credit.get_from(self.description)

    def __str__(self):
        return f"Date: {self.date}. Description: {self.description}. Amount: {self.amount}. Balance: {self.balance}. Type: {self.type.value}"

    def to_csv(self):
        return f"{self.type.value[0]}, {self.date}, {self.description}, {self.amount}, {self.balance}"


class TransactionBuilder:

    def __init__(self):
        self.date = None
        self.description = None
        self.amount = None
        self.balance = None

    def with_date(self, date):
        self.date = date

    def with_description(self, desc):
        self.description = desc

    def with_amount(self, amount):
        self.amount = self.remove_currency(amount)

    def with_balance(self, balance):
        self.balance = self.remove_currency(balance)

    def remove_currency(self, amount):
        return amount.split("GBP")[0].strip()

    def build(self):
        return Transaction(self.date, self.description, self.amount, self.balance)


class TransactionsPeriodSummary:
    headers = ['Category', '#', 'Total (£)']

    class Type(Enum):
        OUT = 'Expense', Expense
        IN = 'Credit', Credit
        ALL = 'Expense and Credit', None

    def __init__(self, period, transactions, summary_type):
        self.period = period
        self.summary_type = summary_type
        self.transactions_for_period = [tran for tran in transactions if self.period in tran.date]
        self.rows = self.calculate_rows()
        self.totals = self.calculate_totals()

    def calculate_rows(self):
        if self.summary_type is not TransactionsPeriodSummary.Type.ALL:
            return self.group_by_category(self.transactions_for_period, self.summary_type.value[1])
        else:
            res = self.group_by_category(self.transactions_for_period, Credit)
            res.extend(self.group_by_category(self.transactions_for_period, Expense))
            return res

    def group_by_category(self, transactions, summary_type):
        """
        :param transactions: a list of Transaction objects
        :param summary_type: Credit or Expense
        :rtype: array of tuples of the form (ExpenseOrCreditType, NoTransactions, Amount). Eg. (Bill, 4, -57.45)
        """
        hits_total_category_rows = []
        for trans_type in summary_type:
            transactions_for_type = [tran for tran in transactions if tran.type == trans_type]
            total_for_category = sum([tran.amount for tran in transactions_for_type])
            row = trans_type.value[0], len(transactions_for_type), round(total_for_category, 2)
            hits_total_category_rows.append(row)
        return hits_total_category_rows

    def calculate_totals(self):
        total_transactions = sum([row[1] for row in self.rows])
        total_amounts = sum([row[2] for row in self.rows])
        return ['', total_transactions, round(total_amounts, 2)]

    # Public APIs
    def print_details_of(self, expense_or_credit_type):
        print(f'\n{expense_or_credit_type.value[0]} transactions detail within {self.period}:')
        [print(tran.to_csv()) for tran in self.transactions_for_period if tran.type == expense_or_credit_type]

    def print(self):
        SummaryPrinter(self.period, TransactionsPeriodSummary.headers, self.rows, self.totals).print_summary()
