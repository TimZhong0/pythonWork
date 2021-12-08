import datetime

import pygame as pygame

from tkinter import *
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

# def print_month_title(year, month):
#     # 打印日历的首部
#     print('         ', get_month_name(month), '   ', year, '          ')
#
#     print('-------------------------------------')
#
#     print('  Mon  Tue  Wed  Thu  Fri  Sat  Sun  ')

def print_month_body(year, month):
    # 打印日历正文
    i = get_start_day(year, month)

    if i % 7 != 1:
        print(' ', end=''),

        print('   ' * i, end=''),
    else:
        print('', end='')

    for j in range(1, get_num_of_days(year, month) + 1):
        print('%5d' % j, end='')


        if i % 7 == 0:  
            print('')

        i += 1

def scream():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

#   主函数部分



month = datetime.datetime.now().month
month1 = str(month)
year = datetime.datetime.now().year
year1 = str(year)
print("当前年", year)
print("当前月", month, "月")
# print_month_title(year, month)
print_month_body(year, month)

# 头部文件
root = Tk()
root.geometry('260x500')
text1 = Text(root, width=100, height=1)
text2 = Text(root, width=100, height=1)
text3 = Text(root, width=100, height=1)
head1 = ['         ' + get_month_name(month) + '   ' + str(year) + '          ']
text1.pack()
text1.insert(INSERT, head1)
head2 = '''-------------------------------------'''
text2.pack()
text2.insert(INSERT, head2)
head3 = '''  Mon  Tue  Wed  Thu  Fri  Sat  Sun  '''
text3.pack()
text3.insert(INSERT, head3)


root.mainloop()