from transactions import TransactionBuilder


def get_transactions_from_txt_export(file_name):
    """
    Reads a Santander TXT transaction file export.
    Expected transaction format:

    Date: 12/09/2019
    Description: MARKS&amp;SPENCER PLC SF (VIA APPLE PAY), ON 10-09-2019
    Amount: -4.10 
    Balance: 131.34

    :param file_name:
    :return: a Transaction
    """
    transactions = []
    with open(file_name) as file:
        transaction_builder = TransactionBuilder()
        for line in file:
            if 'Date:' in line:
                transaction_builder.with_date(line[6:].strip())
            elif 'Description' in line:
                transaction_builder.with_description(line[13:].strip())
            elif 'Amount' in line:
                transaction_builder.with_amount(line[8:].strip())
            elif 'Balance' in line:
                transaction_builder.with_balance(line[9:].strip())
                transactions.append(transaction_builder.build())
    return transactions
