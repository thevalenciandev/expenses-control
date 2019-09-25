from expense import Expense
from santander_transactions_parser import get_transactions_from_txt_export
from stats import YearlyStats
from transactions import TransactionsPeriodSummary

if __name__ == '__main__':
    all_time_transactions = get_transactions_from_txt_export('C:/Temp/Santander_statement.txt')

    # Stats per expense/credit type
    # YearlyStats('2019', all_time_transactions, Expense.HOUSEKEEPING_COSTS).print()

    # for expense in Expense:
    #     YearlyStats('2019', all_time_transactions, expense).print()

    # Yearly PnL per month
    YearlyStats('2019', all_time_transactions).print()

    # MONTHLY SUMMARIES
    # june_expenses = TransactionsPeriodSummary('/06/2019', TransactionsPeriodSummary.Type.OUT, all_time_transactions)
    # june_expenses.print()
    # june_expenses.print_details_of(Expense.HOUSE_GOODS)

    # july_expenses = TransactionsPeriodSummary('/07/2019', TransactionsPeriodSummary.Type.OUT, all_time_transactions)
    # july_expenses.print()

    # august_expenses = TransactionsPeriodSummary('/08/2019', TransactionsPeriodSummary.Type.OUT, all_time_transactions)
    # august_expenses.print()

    # august_credit = TransactionsSummary('/08/2019', TransactionsSummary.Type.IN, all_time_transactions)
    september_expenses = TransactionsPeriodSummary('/09/2019', all_time_transactions,
                                                   TransactionsPeriodSummary.Type.OUT)
    september_expenses.print()
    september_expenses.print_details_of(Expense.UNKNOWN)

    # COMPARISONS
    # TransactionsSummaryComparator(june_expenses, july_expenses).print()
    # TransactionsSummaryComparator(july_expenses, august_expenses).print()
    # TransactionsSummaryComparator(august_expenses, september_expenses).print()
