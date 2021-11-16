import csv
import os

class Group1:
    def __init__(self, file):
        self.file = file

    def write(self,dict_object):
        with open(self.file, 'a') as write_file:
            with open(self.file, 'w', newline='') as outcsv:
                writer = csv.DictWriter(outcsv, fieldnames=[])
            writer.writeheader()
            writer = csv.writer(write_file)
        return self.file

    def delete(self, delete_obj):
        with open(self.file, 'r') as file:
            if os.delete_obj.exists(file):
                os.remove(file)
        return self.file

    def read(self):
        with open(self.file, 'r') as read_file:
            reader = csv.reader(read_file)
        return reader

    def edit(self,edit_key):
        pass
