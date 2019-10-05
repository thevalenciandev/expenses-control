from transactions import TransactionBuilder

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
          'Nov': 11, 'Dec': 12}


def print_santander_txt_export_from_santander_pdf_copy_paste(file_name, year):
    """
    Reads a Santander PDF copy paste.
    Expected format:
    1st May DIRECT DEBIT PAYMENT TO THAMES WATER REF 9482108126, MANDATE NO 0024 31.26 1,234.56

    The above example input would print to console:
    Date: 01/05/2019
    Description: DIRECT DEBIT PAYMENT TO THAMES WATER REF 9482108126, MANDATE NO 0024
    Amount: -31.26
    Balance: 1,234.56

    :param file_name:
    """
    for line in reversed(list(open(file_name))):
        chunks = line.split()
        date_month = chunks[:2]
        print_date(date_month[0], date_month[1], str(year))
        print_description(chunks[2:-2])
        print(f'Amount: -{figure(chunks[-2:-1][0])}')
        print(f'Balance: {figure(chunks[-1:][0])}')
        print()


def figure(chunk):
    return chunk.replace(',', '')


def print_description(description):
    desc = ' '.join(description)
    print(f'Description: {desc}')


def print_date(day, month, year):
    d = day.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '')
    date = '{0}/{1}/{2}'.format(d.zfill(2), str(months[month]).zfill(2), year)
    print(f'Date: {date}')


def get_transactions_from_txt_export(file_name):
    """
    Reads a Santander TXT transaction file export.
    Expected transaction format:

    Date: 12/09/2019
    Description: MARKS&amp;SPENCER PLC SF (VIA APPLE PAY), ON 10-09-2019
    Amount: -4.10 
    Balance: 131.34

    :param file_name:
    :return: an array of Transactions
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
