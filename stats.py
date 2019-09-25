from statistics import mean, median, stdev

from summary_printer import SummaryPrinter


class YearlyStats:

    def __init__(self, year, transactions, transaction_type=None):
        self.year = year
        self.transaction_type = transaction_type
        self.stats_crunched = transaction_type.value[0] if transaction_type is not None else 'PnL'
        predicate = self.filter_by(transaction_type) if transaction_type is not None else self.do_not_filter()
        self.month_year_totals = self.calculate_totals_for(year, filter(predicate, transactions))
        totals = list(self.month_year_totals.values())
        self.mean = mean(totals)
        self.median = median(totals)
        self.stdev = stdev(totals)

    def filter_by(self, transaction_type):
        return lambda tran: tran.type == transaction_type

    def do_not_filter(self):
        return lambda x: True

    def calculate_totals_for(self, year, transactions):
        month_year_totals = {'/{0}/{1}'.format(str(month).zfill(2), year): 0 for month in range(1, 13)}
        for tran in transactions:
            month_year = tran.date[2:]
            month_year_totals[month_year] += tran.amount

        return {month[1:3]: round(amount, 2) for month, amount in month_year_totals.items()}

    def print(self):
        SummaryPrinter('{0}: {1}'.format(self.year, self.stats_crunched),
                       list(self.month_year_totals.keys()),
                       [list(self.month_year_totals.values())],
                       footer='Mean: {0} - Median: {1} - St.dev.: {2}'.format(round(self.mean, 2),
                                                                              round(self.median, 2),
                                                                              round(self.stdev, 2))).print_summary()
