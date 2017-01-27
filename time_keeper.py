from datetime import *
import calendar
calendar.setfirstweekday(calendar.MONDAY)

weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


def set_semester():
    # start_date = date(int(input('Semester begins\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    start_date = date(2016, 9, 26)
    # end_date = date(int(input('Semester ends\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    end_date = date(2017, 1, 25)
    # print('Semester starts on',weekdays[calendar.weekday(start_date[0], start_date[1], start_date[2])])
    print('Semester starts on', weekdays[start_date.weekday()], start_date)
    # print('Semester ends on', weekdays[calendar.weekday(end_date[0], end_date[1], end_date[2])])
    print('Semester ends on', weekdays[end_date.weekday()], end_date)
    diff = end_date - start_date
    print('Semester is ', diff.days , 'long.\n')

    x = start_date
    weeknumber = 1
    while x <= end_date:
        print(x, 'is a', weeknumber, weekdays[x.weekday()])
        x += + timedelta(days=1)
        if x.weekday() == 0:
            weeknumber += 1
            print('\n')
            continue


# retrieves current date/time
# today = datetime.today()
# print(datetime.weekday(today))


set_semester()
