import csv
import os


class WorkingWithFile:

    @staticmethod
    def writing_file(file_name, dict_1):
        with open(file_name, 'w') as csv_file:
            fieldnames = list(dict_1.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if file_name.tell() == 0:
                writer.writeheader()
            writer.writerow(dict_1.values())

    @staticmethod
    def editing_file(file_name):
        with open(file_name, "a") as f:
            f.write("new line\n")
        with open(file_name, "r+") as f:
            old = f.read()  # read everything in the file
        f.seek(0)  # rewind
        f.write("new line\n" + old)  # write the new line before

    @staticmethod
    def reading_file(file_name, dict_1):
        with open(file_name, 'r') as csv_file:
            fieldnames = list(dict_1.keys())
            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            for row in reader:
                print(row)

    @staticmethod
    def delete_line_by_full_match(original_file, line_to_delete):
        """ In a file, delete the lines at line number in given list"""
        is_skipped = False
        dummy_file = original_file + '.bak'
        # Open original file in read only mode and dummy file in write mode
        with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Line by line copy data from original file to dummy file
            for line in read_obj:
                line_to_match = line
                if line[-1] == '\n':
                    line_to_match = line[:-1]
                # if current line matches with the given line then skip that line
                if line_to_match != line_to_delete:
                    write_obj.write(line)
                else:
                    is_skipped = True
        # If any line is skipped then rename dummy file as original file
        if is_skipped:
            os.remove(original_file)
            os.rename(dummy_file, original_file)
        else:
            os.remove(dummy_file)


class Task:
    def __init__(self, title, date, category, description, importance, clock_reminder, is_done=False):
        self.title = title
        self.date = date
        self.category = category
        self.description = description
        self.importance = importance
        self.clock_reminder = clock_reminder
        self.is_done = is_done

    def task_is_done(self):
        if not self.is_done:
            self.is_done = True
        else:
            print(f"The {self.title} is {self.is_done}")
        return True

    def file(self):
        with open('task.csv', 'a') as csv_file:
            fieldnames = ['title', 'date', 'category', 'description', 'importance', 'clock_reminder', 'is_done']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'title': self.title, 'date': self.date, 'category': self.category,
                             'description': self.description, 'importance': self.importance,
                             'clock_reminder': self.clock_reminder, 'is_done': self.is_done})

        def edit_task(self, input_dic):
            if input_dic['title'] != None:
                self.title = input_dic['title']
            self.date = input_dic['date']
            self.category = input_dic['category']
            self.importance = input_dic['importance']
            self.clock_reminder = input_dic['clock_reminder']

        def __str__(self):
            return f'{self.title} is {self.is_done} on {self.date}'

    list_tasks = []

    def print_tasks():
        for i, task in enumerate(list_tasks):
            print(f'{i + 1}:  {task}')

    def get_data():
        title, date, category, description, importance, clock_reminder = input(
            'Enter title, date, category, description,'
            ' importance, clock_reminder:').split(',')
        task = Task(title, date, category, description, importance, clock_reminder)
        return task

    def delete_object(a):
        del a

    while True:
        x = input('What would you like to do? ')
        if x == '1':
            new_abject = get_data()
            list_tasks.append(new_abject)
            new_abject.file()
        elif x == '2':
            print_tasks()

        elif x == '3':
            print_tasks()
            t = int(input('Which one task do you want to remove?: '))
            if Task.task_is_done(list_tasks[t - 1]):
                del list_tasks[t - 1]
            print_tasks()
        elif x == '4':
            print_tasks()
            t = int(input('Which one task do you want to edit?: '))
            dic_edit = {'title': None, 'date': None, 'category': None, 'importance': None, 'clock_reminder': None}
            edit = input('1- title\n2- date\n3- category\n4- importance\n5- clock reminder\n??: ')
            if edit == '1':
                edit_title = input('Enter your title: ')
                dic_edit['title'] = edit_title
                list_tasks[t - 1].edit_task(dic_edit)
        elif x == '5':
            break

    delete_object(list_tasks[1])
