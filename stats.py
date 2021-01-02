from statistics import mean, median, stdev
from summary_printer import SummaryPrinter


class YearlyStats:

    def __init__(self, year, transactions, transaction_type=None):
        self.year = year
        self.category = transaction_type.value[0] if transaction_type is not None else 'PnL'
        self.month_year_totals = self.calculate_totals(transactions, transaction_type)
        totals = list(self.month_year_totals.values())
        self.mean = mean(totals)
        self.median = median(totals)
        self.stdev = stdev(totals)
        self.total = sum(totals)

    def calculate_totals(self, transactions, transaction_type):
        transactions = transactions if transaction_type is None else filter(lambda tran: tran.type == transaction_type, transactions)
        month_year_totals = {'/{0}/{1}'.format(str(month).zfill(2), self.year): 0 for month in range(1, 13)}
        for tran in transactions:
            month_year = tran.date[2:]
            month_year_totals[month_year] += tran.amount

        return {month[1:3]: round(amount, 2) for month, amount in month_year_totals.items()}

    def print(self):
        SummaryPrinter(title='{0}: {1}'.format(self.year, self.category),
                       headers=list(self.month_year_totals.keys()),
                       rows=[list(self.month_year_totals.values())],
                       footer='Mean: {0} - Median: {1} - St.dev.: {2} - Total: {3}'
                       .format(round(self.mean, 2),
                               round(self.median, 2),
                               round(self.stdev, 2),
                               round(self.total, 2))) \
            .print_summary()
