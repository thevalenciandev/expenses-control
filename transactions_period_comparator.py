from summary_printer import SummaryPrinter


class TransactionsSummaryComparator:
    headers = ['Category', 'Delta #', 'Delta Total (£)']

    def __init__(self, from_summary, to_summary):
        self.from_summary = from_summary
        self.to_summary = to_summary
        self.rows = self.compare_summary_rows()
        self.totals = self.compare_summary_totals()
        self.title = self.from_summary.period + ' ---> ' + self.to_summary.period + ' (Negative values are good)'

    def compare_summary_rows(self):
        """
        Each row is a tuple of the form (NoTransactions, Amount, CreditOrExpenseType). Eg. (4, -57.45, Bill)
        :return: an array of tuples of the form (CreditOrExpenseType, NoTransDiff, AmountDiff). Eg. (-1, -11.93, Bill)
        """
        comparison = []
        for from_row, to_row in zip(self.from_summary.rows, self.to_summary.rows):
            if from_row[0] != to_row[0]:
                raise Exception(f'Cannot compare different transaction categories. {from_row[0]} <> {to_row[0]}')
            category = from_row[0]
            no_transaction_diff = to_row[1] - from_row[1]
            amount_diff = from_row[2] - to_row[2]
            comparison.append((category, no_transaction_diff, round(amount_diff, 2)))
        return comparison

    def compare_summary_totals(self):
        no_transaction_total_diff = -(self.from_summary.totals[1] - self.to_summary.totals[1])
        amount_totals_diff = self.from_summary.totals[2] - self.to_summary.totals[2]
        return ['', no_transaction_total_diff, round(amount_totals_diff, 2)]

    def print(self):
        SummaryPrinter(self.title, TransactionsSummaryComparator.headers,
                       self.rows,
                       self.totals).print_summary()
