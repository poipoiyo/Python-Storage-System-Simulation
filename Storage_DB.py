import pymongo
from pymongo import MongoClient
import tkinter as tk

# basic window set
window = tk.Tk()
window.title("Storage System")
window.geometry("1080x600")
window.resizable(0,0)

# connect to MongoDB

uri = "mongodb+srv://<username>:<password>@cluster0-qnhak.mongodb.net/<database>"
client = MongoClient(uri)
db = client['test']
collection = db['python']

# find from database
def db_find():
    empty1.set('')
    Name = Name_blank.get()
    if Name == '' :
        warning.set('fill in the name')
        return
    target = collection.find_one({'Name': Name})

    if target is None :
        warning.set(' not here ')
    else :
        warning.set(str(target['Amount']) + ' ' + Name + ' left ')

# input to database
def db_in():
    empty3.set('')
    Name = Name1_blank.get()
    Num = Num1_blank.get()

    try :
        num = int(Num)
    except :
        warning.set('fill in correct id and amount')

    if Name == '' or Num == '' or int(Num) <= 0:
        warning.set('fill in correct id and amount')
        return
    num = int(Num)
    Box = { 'Name': Name, 'Amount': num }

    target = collection.find_one({ 'Name': Name })

    if target is None :
        collection.insert(Box)
        warning.set(' save ' + Name + ' * ' + Num + ' in ')
    else :
        target['Amount'] += num
        collection.update({ 'Name': Name }, target)
        warning.set(' increase ' + Name + ' * ' + Num)

# output from database
def db_out():
    empty2.set('')
    Name = Name2_blank.get()
    Num = Num2_blank.get()

    try:
        num = int(Num)
    except:
        warning.set('fill in correct id and amount')

    if Name == '' or Num == '' or int(Num) <= 0:
        warning.set('fill in correct id and amount')
        return
    num = int(Num)

    target = collection.find_one({'Name': Name})
    if target is None :
        warning.set('Not here')
    else :
        if target['Amount'] < num :
            warning.set('Not enough')
        elif target['Amount'] == num:
            collection.delete_one({'Name': Name})
            warning.set(' decrease ' + Name + ' * ' + Num + ' , and it is empty')
        else:
            target['Amount'] -= num
            collection.update({ 'Name': Name }, target)
            warning.set(' decrease ' + Name + ' * ' + Num)

# arrange labels, buttons

empty1 = tk.StringVar()
empty2 = tk.StringVar()
empty3 = tk.StringVar()

Name_blank = tk.Entry(window,textvariable=empty1,text="ID",font=('Arial',18),fg='gray')
Name1_blank = tk.Entry(window,textvariable=empty2,text="ID1",font=('Arial',18),fg='gray')
Name2_blank = tk.Entry(window,textvariable=empty3,text="ID2",font=('Arial',18),fg='gray')
Num1_blank = tk.Entry(window,textvariable=empty2,text="Amount1",font=('Arial',18),fg='gray')
Num2_blank = tk.Entry(window,textvariable=empty3,text="Amount2",font=('Arial',18),fg='gray')

Hint = tk.Label(window,text='Can find, incearse, decrease items as a simple storage system '
                ,background='gray',font=('3ds', 24))
Name1 = tk.Label(window,text='Name1',background='gray',font=('3ds', 24))
Name2 = tk.Label(window,text='Name2',background='gray',font=('3ds', 24))
Num1 = tk.Label(window,text='Amount1',background='gray',font=('3ds', 24))
Num2 = tk.Label(window,text='Amount2',background='gray',font=('3ds', 24))
Label1 = tk.Label(window,text='-->',background='gray',font=('3ds', 24))
Label2 = tk.Label(window,text='-->',background='gray',font=('3ds', 24))
Label3 = tk.Label(window,text='-->',background='gray',font=('3ds', 24))
Find_button = tk.Button(window, text="Find by name",font=('3ds',20) ,command=db_find)
OK_button1 = tk.Button(window, text="Save in",font=('3ds',20) ,command=db_in)
OK_button2 = tk.Button(window, text="Take out",font=('3ds',20) ,command=db_out)

Hint.grid(row=0,column=0,columnspan=4,ipadx=80,padx=10,pady=20)
Name1.grid(row=2,column=1,ipadx=80,padx=10,pady=20)
Name2.grid(row=4,column=1,ipadx=80,padx=10,pady=10)
Num1.grid(row=2,column=2,ipadx=40,padx=0,pady=20)
Num2.grid(row=4,column=2,ipadx=40,padx=10,pady=10)
Label1.grid(row=1,column=0,ipadx=40,padx=50,pady=50)
Label2.grid(row=3,column=0,ipadx=40,padx=10,pady=10)
Label3.grid(row=5,column=0,ipadx=40,padx=10,pady=10)

Name_blank.grid(row=1,column=1,padx=10,pady=20)
Name1_blank.grid(row=3,column=1,padx=10,pady=20)
Name2_blank.grid(row=5,column=1,padx=10,pady=20)
Num1_blank.grid(row=3,column=2,padx=10,pady=20)
Num2_blank.grid(row=5,column=2,padx=10,pady=20)

Find_button.grid(row=1,column=2,ipadx=40,padx=10,pady=20)
OK_button1.grid(row=3,column=3,ipadx=40,padx=10,pady=20)
OK_button2.grid(row=5,column=3,ipadx=40,padx=10,pady=20)

warning = tk.StringVar()
warning.set('Result shows here')
Label3 = tk.Label(window,textvariable=warning,text='', font=('3ds', 20))
Label3.grid(row=6,column=0,columnspan=4,ipadx=300,pady=20)

# execute
window.mainloop()




