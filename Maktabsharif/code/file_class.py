import csv

"""
    File class
"""


class File:
    def __init__(self, url):
        self.url = url

    def write_to_file(self, **data):
        with open(self.url, mode='w') as csv_file:
            fieldnames = list(data.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

    def read_file(self):
        with open(self.url, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                    header = row.keys()
                    print(row)
                for i in header:
                    print(f'{i}:{row[i]}', end=',')
                print()
                line_count += 1
            print(f'Processed {line_count} lines.')

    def append_to_file(self, **data):
        fieldnames = list(data.keys())
        with open(self.url, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(data)

    def delete_from_file(self, row_input):
        with open(self.url, 'r') as inp, open('users_new_01.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                print(row)
                print(row[row_input])
                print(row_input)
                if row == row_input:
                    writer.writerow(row)


url_input = 'users.csv'
dict_data = {'first_name': 'Mina', 'last_name': 'Hasani', 'age': '23'}
file = File(url_input)
file.read_file()
file.append_to_file(first_name='Mina', last_name='Hasani', age=23)
row_input_user = int(input('enter the row: '))
file.delete_from_file(row_input_user)

