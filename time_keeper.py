from datetime import *

en_weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
pl_weekdays = ['Pn', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']
pl_en_weekdays = {'Pn': 'MON', 'Wt': 'TUE', 'Śr': 'WED', 'Czw': 'THU', 'Pt': 'FRI', 'Sb': 'SAT', 'Nd': 'SUN'}


def set_term():
    # term_start = date(int(input('Semester begins\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    # term_end = date(int(input('Semester ends\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    term_start = date(2016, 9, 26)
    term_end = date(2017, 1, 25)

    # holidays_start = date(int(input('Holidays begin\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    # holidays_end = date(int(input('Holidays end\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    holidays_start = date(2016, 12, 22)
    holidays_end = date(2017, 1, 2)

    show_term_info(term_start, term_end, holidays_start, holidays_end)

    return [term_start, term_end, holidays_start, holidays_end]


def show_term_info(term_start, term_end, holidays_start, holidays_end):
    print('\nSemester starts on', en_weekdays[term_start.weekday()], term_start)
    print('Semester ends on', en_weekdays[term_end.weekday()], term_end)

    print('\nHolidays start on', en_weekdays[holidays_start.weekday()], holidays_start)
    print('Holidays end on', en_weekdays[holidays_end.weekday()], holidays_end)

    delta = term_end - term_start
    print('\nSemester is', delta.days, 'days long.')


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
