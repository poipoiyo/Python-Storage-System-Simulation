import pymongo
from pymongo import MongoClient
import tkinter as tk

# basic window set
window = tk.Tk()
window.title("What's here")
window.geometry("720x600")
window.resizable(0,0)

Hint = tk.Label(window,text='View all the items here'
                ,background='gray',font=('3ds', 24))
Hint.grid(row=0,column=0,ipadx=200,padx=10,pady=20)

Text = tk.StringVar()
Text.set('')
Label = tk.Label(window,textvariable=Text,text='', font=('3ds', 24))
Label.grid(row=1,column=0,pady=20)



# connect to MongoDB

uri = "mongodb+srv://Poiguy:Mongodb877@cluster0-qnhak.mongodb.net/payment"
client = MongoClient(uri)
db = client['test']
collection = db['python']

results = collection.find()
item = ''
count = 1
for result in results:
    item += ' Item' + str(count) + ': ' + result['Name'] + ' left ' + str(result['Amount']) + ' in database.\n'
    item += ' \n'
    count += 1
Text.set(item)

def refresh():
    results = collection.find()
    item = ''
    count = 1
    for result in results:
        item += ' Item' + str(count) + ': ' + result['Name'] + ' left ' + str(result['Amount']) + ' in database.\n'
        item += ' \n'
        count += 1
    Text.set(item)


Refresh_button = tk.Button(window, text="Refresh",font=('3ds',20) ,command=refresh)
Refresh_button.grid(row=2,column=0,ipadx=40,padx=10,pady=20)

# execute
window.mainloop()