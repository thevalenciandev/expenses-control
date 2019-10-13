from labels import Label
from santander_transactions_parser import get_transactions_from_txt_export
from transactions import TransactionsPeriodSummary
from transactions_period_comparator import TransactionsSummaryComparator

import sys

if __name__ == '__main__':
    export_file = sys.argv[1]
    print(f'Processing export file {export_file}...')
    all_time_transactions = get_transactions_from_txt_export(export_file)

    # MONTHLY SUMMARIES
    jan_transactions = TransactionsPeriodSummary('/01/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # jan_transactions.print()

    feb_transactions = TransactionsPeriodSummary('/02/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # feb_transactions.print()

    mar_transactions = TransactionsPeriodSummary('/03/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # mar_transactions.print()

    apr_transactions = TransactionsPeriodSummary('/04/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # apr_transactions.print()

    may_transactions = TransactionsPeriodSummary('/05/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # may_transactions.print()

    june_transactions = TransactionsPeriodSummary('/06/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # june_transactions.print()

    july_transactions = TransactionsPeriodSummary('/07/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # july_transactions.print()

    august_transactions = TransactionsPeriodSummary('/08/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # august_transactions.print()

    sept_transactions = TransactionsPeriodSummary('/09/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    # sept_transactions.print()

    oct_transactions = TransactionsPeriodSummary('/10/2019', all_time_transactions, TransactionsPeriodSummary.Type.ALL)
    oct_transactions.print()

    # DETAILS OF A SPECIFIC CATEGORY/LABEL
    for label in Label:
        oct_transactions.print_details_of(label)

    # COMPARISONS
    # TransactionsSummaryComparator(jan_transactions, feb_transactions).print()
    # TransactionsSummaryComparator(feb_transactions, mar_transactions).print()
    # TransactionsSummaryComparator(mar_transactions, apr_transactions).print()
    # TransactionsSummaryComparator(apr_transactions, may_transactions).print()
    # TransactionsSummaryComparator(may_transactions, june_transactions).print()
    # TransactionsSummaryComparator(june_transactions, july_transactions).print()
    # TransactionsSummaryComparator(july_transactions, august_transactions).print()
    # TransactionsSummaryComparator(august_transactions, sept_transactions).print()
    TransactionsSummaryComparator(sept_transactions, oct_transactions).print()
