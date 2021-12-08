import datetime

from tkinter import *

win = Tk()
win.geometry('260x200+500+200')

def show():
    print(year1.get())
    print(month1.get())
    win.quit()

tVar1 = StringVar()
tVar2 = StringVar()

l1 = Label(win, text="年份: ")
l1.pack()

year1 = Entry(win, textvariable=tVar1)
year1.pack()


l2 = Label(win, text="月份: ")
l2.pack()

month1 = Entry(win, textvariable=tVar2)
month1.pack()


button = Button(win, text='按钮', command=show)

button.pack()

win.mainloop()

def is_leap_year(year):
    # 判断是否为闰年
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_num_of_days(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap_year(year):
        return 29  # 闰年2月
    else:
        return 28  # 平年2月

def get_total_days(year,month):
    days = 0
    for y in range(1800, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += get_num_of_days(year, m)

    return days

def get_start_day(year, month):
    # 返回当月1日是星期几，由1800.01.01是星期三推算
    return 3 + get_total_days(year, month) % 7

month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

def get_month_name(month):
    # 返回当月的名称
    return month_dict[month]

def print_month_title(year, month):
    # 打印日历的首部
    print('         ', get_month_name(month), '   ', year, '          ')

    print('-------------------------------------')

    print('  Mon  Tue  Wed  Thu  Fri  Sat  Sun  ')

def print_month_body(year, month):
    # 打印日历正文
    i = get_start_day(year, month)
    # print(i)
    if i % 7 != 1:
        print(' ', end=''),  # 打印行首的两个空格

        print('   ' * i, end=''),  # 从星期几开始则空5*几个空格
    else:
        print('', end='')  # 打印行首的两个空格

    for j in range(1, get_num_of_days(year, month) + 1):
        print('%5d' % j, end='')  # 宽度控制，4+1=5


        if i % 7 == 0:  # i用于计数和换行
            print('')  # 每换行一次行首继续空格

        i += 1

#   主函数部分
month = int(month1.get())
year = int(year1.get())
print("当前年", year)
print("当前月", month, "月")
print_month_title(year, month)
print_month_body(year, month)




root = Tk()
root.geometry('260x200+500+200')

def die():
    win.destroy()
    root.destroy()

text1 = Text(root, width=36, height=1)
text2 = Text(root, width=36, height=1)
text3 = Text(root, width=36, height=1)
text4 = Text(root, width=36, height=6)

head1 = ['         ' + get_month_name(month) + '   ' + str(year) + '          ']
text1.grid(row=1, column=0)
text1.insert(INSERT, head1)
head2 = '''-------------------------------------'''
text2.grid()
text2.insert(INSERT, head2)
head3 = '''  Mon  Tue  Wed  Thu  Fri  Sat  Sun  '''
text3.grid()
text3.insert(INSERT, head3)

# 日历正文
global body
i = get_start_day(year, month)

if i % 7 != 1:
    # print(' ', end=''),
    body = ' '
    # print('   ' * i, end=''),
    body += '   ' * (i)
else:
    # print('')# 换行
    body += '\n'

for j in range(1, get_num_of_days(year, month) + 1):
    # print('%5d' % j, end='')
    body += '%5d' % j
    if i % 7 == 0:
        print('')# 换行
        body += '\n'

    i += 1
text4.grid()
text4.insert(INSERT, body)

button1 = Button(root, text='结束', command=die)
button1.grid()


root.mainloop()