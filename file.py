import csv
from csv import DictWriter
class File:
    def __init__(self, path):
        self.path = path
    def write_file(self,dict_w):
        key = list(dict_w.keys())
        with open(self.path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=key)
            if csvfile.tell()==0:
                writer.writeheader()
            writer.writerows([dict_w])
a = {"a": "d","s": "f"}
f1 = File("Book1.csv")
f1.write_file(a)