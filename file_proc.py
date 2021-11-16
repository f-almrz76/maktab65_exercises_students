import csv


class File_process:
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                list_content = [item for item in csv_reader]
        except Exception as ex:
            print(ex)
        return list_content

    def write(self, content):
        try:
            with open(self.path, 'w', newline='') as csvfile:
                fieldnames = ['title', 'date', 'category', 'importance', 'clock_reminder']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if len(open(self.path).readlines())== 0:
                    writer.writeheader()
                for i in content:
                    writer.writerow(i)
        except Exception as ex:
            print(ex)
        return

    def edit(self , dic):
        content = self.read()
        for i in content:
            if dic['title'] == i['title']:
                for j , item in enumerate(dic.keys()):
                    i[j] = item
        self.write(content)
        return

    def remove(self , title):
        content = self.read()
        for i in content:
            if i['title'] == title:
               del i

        self.write(content)
        return
f1 = File_process("task.csv")
f1.write([{'title':1, 'date':2, 'category':3, 'importance':4, 'clock_reminder':5},{'title':2, 'date':2, 'category':3, 'importance':4, 'clock_reminder':6}])
print(f1.read())
f1.edit({'title':1,'date':10})
print(f1.read())
f1.remove(1)
print(f1.read())