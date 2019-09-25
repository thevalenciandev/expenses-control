class SummaryPrinter:
    col_padding = 5
    space_length = 1  # one ' ' for columns that need it
    col_sep_length = 1  # one '|' for columns that need it (TODO: need to make the '|' a class variable)

    def __init__(self, title, headers, rows, totals=None, footer=None):
        self.col_lengths = self.calculate_col_lengths(headers, rows)
        self.line_size = self.calculate_line_size()
        self.title = title
        self.headers = headers
        self.rows = rows
        self.totals = totals
        self.footer = footer

    def calculate_col_lengths(self, headers, rows):
        lengths = []
        for index in range(len(headers)):
            lengths.append(self.calculate_col_length(index, headers, rows))
        return lengths

    def calculate_col_length(self, index, headers, rows):
        longest_col = max([len(str(row[index])) for row in rows])
        return max(len(headers[index]), longest_col) + self.col_padding

    def calculate_line_size(self):
        size = 0
        for index in range(len(self.col_lengths) - 1):
            size = size + self.col_lengths[index] + self.space_length + self.col_sep_length
        return size + self.col_lengths[len(self.col_lengths) - 1] + self.space_length

    def print_summary(self):
        self.print_top_line()
        self.print_title()

        self.print_line_with_separators(sep='_')
        self.print_headers()
        self.print_line_with_separators()

        self.print_all_rows()

        if self.totals is not None:
            self.print_totals()

        if self.footer is not None:
            self.print_footer()

        print()  # Just an extra separation

    def print_title(self):
        title = self.align_center(self.line_size).format(self.title)
        print(f'|{title}|')

    def print_footer(self):
        self.print_line_with_separators()
        footer = self.align_center(self.line_size).format(self.footer)
        print(f'|{footer}|')
        self.print_line_with_separators(sep='_')

    def print_all_rows(self):
        order_by_column2 = lambda row: row[2]  # TODO: generify
        for row in sorted(self.rows, key=order_by_column2):
            self.print_row(row)

    def print_top_line(self, ):
        print(' ' + '_' * self.line_size)

    def print_headers(self):
        self.print_row(self.headers)

    def print_line_with_separators(self, sep='|'):
        print('|', end='')
        for index, col_length in enumerate(self.col_lengths):
            sep_for_this_column = sep if index < (len(self.col_lengths) - 1) else ''
            print('_' * (col_length + self.space_length) + sep_for_this_column, end='')
        print('|')

    def print_totals(self):
        self.print_line_with_separators()
        contents = ['Totals', '', '']
        self.print_row(contents, sep=' ')
        self.print_line_with_separators(sep='_')
        self.print_row(self.totals)
        self.print_line_with_separators()

    def print_row(self, contents, sep='|'):
        print(sep, end='')
        for col_length, content in zip(self.col_lengths, contents):
            col = self.align_right(col_length).format(content)
            print(f'{col} {sep}', end='')
        print()

    def align_right(self, col_length):
        return '{:>' + str(col_length) + '}'

    def align_center(self, col_length):
        return '{:^' + str(col_length) + '}'
