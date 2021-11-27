import datetime

def shifourunnian(year):
    # 判断是否为闰年
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def panduanyuefen(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif shifourunnian(year):
        return 29  # 闰年2月
    else:
        return 28  # 平年2月

def youjitian(year,month):
    days = 0
    for y in range(1800, year):
        if shifourunnian(y):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += panduanyuefen(year, m)

    return days

def get_start_day(year, month):
    # 返回当月1日是星期几，由1800.01.01是星期三推算
    return 3 + youjitian(year, month) % 7

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
    '''
    打印日历正文
    格式说明：空两个空格，每天的长度为5
    需要注意的是print加逗号会多一个空格
    '''
    i = get_start_day(year, month)
    # print(i)
    if i % 7 != 1:
        print(' ', end=''),  # 打印行首的两个空格

        print('   ' * i, end=''),  # 从星期几开始则空5*几个空格
    else:
        print('', end='')  # 打印行首的两个空格

    for j in range(1, panduanyuefen(year, month) + 1):
        print('%5d' % j, end='')  # 宽度控制，4+1=5


        if i % 7 == 0:  # i用于计数和换行
            print('')  # 每换行一次行首继续空格

        i += 1

#   主函数部分
month = datetime.datetime.now().month
year = datetime.datetime.now().year
print("当前年", year)
print("当前月", month, "月")
print_month_title(year, month)
print_month_body(year, month)