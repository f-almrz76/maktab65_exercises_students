import csv



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

    # def edit_task(self, input_dic):
    #     if input_dic['title'] != None:
    #         self.title = input_dic['title']
    #     self.date = input_dic['date']
    #     self.category = input_dic['category']
    #     self.importance = input_dic['importance']
    #     self.clock_reminder = input_dic['clock_reminder']


    
    def edit_task(self):
        titels=['title','date','category','importance','clock_reminder',]
        key=int(input('select 1)title 2)date 3)category 4)importance 5)clock_reminder'))
        for i,item in enumerate(titels):
            if key == i-1:
                change=self.__dict__
                new=input('your new value')
                change[item]=new
                return change

            
    def __str__(self):
        return f'{self.title} is {self.is_done} on {self.date}'

    def __repr__(self):
        return self.__dict__



class File_writing:
    def __init__(self,made_task):
        self.made_task = made_task

    def writing(self):
        with open('myfile.csv','w') as myfile:
            writer=csv.DictWriter(myfile,fieldnames=['the task'])
            if myfile.tell()==0:
                writer.writeheader()
            writer.writerow(self.made_task)



    # def reading(self):
    #     read_list=[]
    #     with open('myfile.csv','r') as f:
    #         f=csv.DictReader(f,fieldnames=['the task'])
    #         for row in f:
    #             read_list.append(row)



list_tasks = []


def print_tasks():
    for i, task in enumerate(list_tasks):
        print(f'{i + 1}:  {task}')


def get_data():
    title, date, category, description, importance, clock_reminder = input('Enter title, date, category, description,'
                                                                           ' importance, clock_reminder:').split(',')
    task = Task(title, date, category, description, importance, clock_reminder)
    return task

# def delete_object(a):
#     del a









while True:
    x = input('What would you like to do? ')
    if x == '1':
        list_tasks.append(get_data())
    elif x == '2':
        print_tasks()

    elif x == '3':
        print_tasks()
        t = int(input('Which one task do you want to remove?: '))
        if Task.task_is_done(list_tasks[t-1]):
            del list_tasks[t-1]
        print_tasks()
    elif x == '4':
        print_tasks()
        t = int(input('Which one task do you want to edit?: '))
        # dic_edit = {'title':None, 'date': None, 'category': None, 'importance': None, 'clock_reminder': None}
        # edit = input('1- title\n2- date\n3- category\n4- importance\n5- clock reminder\n??: ')
        # if edit == '1':
        #     edit_title = input('Enter your title: ')
        #     dic_edit['title'] = edit_title
        #     list_tasks[t - 1].edit_task(dic_edit)
        for i,item in enumerate(list_tasks):
            if t==i-1:
                item.edit_task()

    elif x == '5':
        break


x=File_writing(list_tasks[0])
print(x)
# x.writing()
# delete_object(list_tasks[1])
