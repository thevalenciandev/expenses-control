from labels import Label
from santander_transactions_parser import get_transactions_from_txt_export
from stats import YearlyStats

import sys

if __name__ == '__main__':
    export_file = sys.argv[1]
    print(f'Processing export file {export_file}')
    all_time_transactions = get_transactions_from_txt_export(export_file)

    # Yearly PnL per month
    YearlyStats('2019', all_time_transactions).print()

    # Stats per Label type
    for label in Label:
        YearlyStats('2019', all_time_transactions, label).print()
