from datetime import *

en_weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
pl_weekdays = ['Pn', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']
pl_en_weekdays = {'Pn': 'MON', 'Wt': 'TUE', 'Śr': 'WED', 'Czw': 'THU', 'Pt': 'FRI', 'Sb': 'SAT', 'Nd': 'SUN'}


def set_term():
    # start_date = date(int(input('Semester begins\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    term_start = date(2016, 9, 26)
    # end_date = date(int(input('Semester ends\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    term_end = date(2017, 1, 25)
    holidays_start = date(2016, 12, 22)
    holidays_end = date(2017, 1, 2)
    # print('Semester starts on',weekdays[calendar.weekday(start_date[0], start_date[1], start_date[2])])
    print('\nSemester starts on', en_weekdays[term_start.weekday()], term_start)
    print('\nHolidays start on', en_weekdays[holidays_start.weekday()], holidays_start)
    print('Holidays end on', en_weekdays[holidays_end.weekday()], holidays_end)
    # print('Semester ends on', weekdays[calendar.weekday(end_date[0], end_date[1], end_date[2])])
    print('\nSemester ends on', en_weekdays[term_end.weekday()], term_end)
    delta = term_end - term_start
    print('Semester is', delta.days, 'days long.')
    return [term_start, term_end, holidays_start, holidays_end]


def divide_by_weeks(term_start, term_end, hol_start, hol_end):

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == hol_start:
            week_num += 1
            print('\nHolidays\n')
            print('Week', week_num)
            i = hol_end + timedelta(days=1)
            continue

        if i.weekday() == 0:
            week_num += 1
            print('\nWeek', week_num)

        if i.weekday() not in [5, 6]:  # skipping weekends
            print(i, 'is', en_weekdays[i.weekday()])
        i += timedelta(days=1)


def get_week_day_index(week_day):
    # week_day_index = list(pl_en_weekdays.keys()).index(week_day)
    week_day_index = pl_weekdays.index(week_day)
    # print('Index of', week_day_index)
    return week_day_index

# retrieves current date/time
# today = datetime.today()
# print(datetime.weekday(today))

# test
# term = set_term()
# divide_by_weeks(term[0], term[1], term[2], term[3])
