from tkinter import *


global year1
global month1

root = Tk()
root.geometry('260x200+500+200')

def show():
    print(year.get())
    print(month.get())
    root.quit()

tVar1 = StringVar()
tVar2 = StringVar()

l1 = Label(root, text="年份: ")
l1.pack()

year = Entry(root, textvariable=tVar1)
year.pack()


l2 = Label(root, text="月份: ")
l2.pack()

month = Entry(root, textvariable=tVar2)
month.pack()


button = Button(root, text='按钮', command=show)

button.pack()

root.mainloop()


print(year.get())
