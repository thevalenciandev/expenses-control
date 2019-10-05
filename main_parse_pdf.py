from santander_transactions_parser import print_santander_txt_export_from_santander_pdf_copy_paste

if __name__ == '__main__':

    # 1. COPY PASTE ALL TRANSACTIONS FROM A SANTANDER PDF AND PUT THEM IN A FILE
    # 2. USE THE FILE AS INPUT BELOW
    # 3. THE OUTPUT OF THIS CAN BE THEN APPENDED TO THE MAIN TRANSACTIONS FILE
    all_time_transactions = print_santander_txt_export_from_santander_pdf_copy_paste(
        'C:/Temp/Santander_pasted_statements.txt', 2019)
