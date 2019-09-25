import re
from enum import Enum


class Credit(Enum):
    # Left value: human readable description
    # Right value: (case un-sensitive) words to match in each transaction, separated by '|' if there are several of them

    # Replace the current 'right' dummy values by the ones that appear in your statement
    # Add more Enums as needed and they'll be automatically picked-up by the expense reports
    CASH_BACK = 'Cashback', 'Cashback'
    INTEREST = 'Interest account', 'INTEREST PAID'
    SALARY = 'Salary', 'EMPLOYER'
    UNKNOWN = 'Unknown (refunds?)', 'Unknown'

    # TODO: DRY!!! Abstract Enums?
    @staticmethod
    def found(transaction_type, desc):
        return re.search(transaction_type.value[1], desc, re.IGNORECASE) is not None

    @staticmethod
    def get_from(desc):
        for tran_type in Credit:
            if Credit.found(tran_type, desc):
                return tran_type
        else:
            return Credit.UNKNOWN
