from labels import Label
from santander_transactions_parser import get_transactions_from_txt_export
from stats import YearlyStats

if __name__ == '__main__':
    all_time_transactions = get_transactions_from_txt_export('C:/Temp/Santander_statement.txt')

    # Yearly PnL per month
    YearlyStats('2019', all_time_transactions).print()

    # Stats per Label type
    for credit in Label:
        YearlyStats('2019', all_time_transactions, credit).print()
