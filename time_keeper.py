from datetime import *

en_weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
pl_weekdays = ['Pn', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']


def set_term():
    # term_start = date(int(input('Semester begins\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    # term_end = date(int(input('Semester ends\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    term_start = date(2016, 9, 26)
    term_end = date(2017, 1, 25)

    # holidays_start = date(int(input('Holidays begin\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    # holidays_end = date(int(input('Holidays end\nYear: ')), int(input('Month: ')), int(input('Day: ')))
    holidays_start = date(2016, 12, 22)
    holidays_end = date(2017, 1, 2)

    term = [term_start, term_end, holidays_start, holidays_end]

    return term


def get_week_day_index(week_day):
    # week_day_index = list(pl_en_weekdays.keys()).index(week_day)
    week_day_index = pl_weekdays.index(week_day)
    # print('Index of', week_day_index)
    return week_day_index


# Not used during runtime, help methods for testing –––––––––––––––––––––––––––––––––––––––––––


pl_en_weekdays = {'Pn': 'MON', 'Wt': 'TUE', 'Śr': 'WED', 'Czw': 'THU', 'Pt': 'FRI', 'Sb': 'SAT', 'Nd': 'SUN'}


def show_term_info(term):

    term_start = term[0]
    term_end = term[1]
    holidays_start = term[2]
    holidays_end = term[3]

    print('\nSemester starts on', en_weekdays[term_start.weekday()], term_start)
    print('Semester ends on', en_weekdays[term_end.weekday()], term_end)

    print('\nHolidays start on', en_weekdays[holidays_start.weekday()], holidays_start)
    print('Holidays end on', en_weekdays[holidays_end.weekday()], holidays_end)

    delta = term_end - term_start
    print('\nSemester is', delta.days, 'days long.')


def divide_by_weeks(term):

    term_start = term[0]
    term_end = term[1]
    holidays_start = term[2]
    holidays_end = term[3]

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == holidays_start:
            week_num += 1
            print('\nHolidays\n')
            print('Week', week_num)
            i = holidays_end + timedelta(days=1)
            continue

        if i.weekday() == 0:
            week_num += 1
            print('\nWeek', week_num)

        if i.weekday() not in [5, 6]:  # skipping weekends
            print(i, 'is', en_weekdays[i.weekday()])
        i += timedelta(days=1)


def create_events_by_day(term, class_title, week_day_index, start_time, end_time, class_type, location, lecturer):

    term_start = term[0]
    term_end = term[1]
    holidays_start = term[2]
    holidays_end = term[3]

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == holidays_start:
            week_num += 1
            print('\nHolidays\n')
            # print('Week', week_num)
            i = holidays_end + timedelta(days=1)
            continue

        if i.weekday() == week_day_index:
            print('\nWeek', week_num)
            print('Class:', class_title)
            print(i, 'Day of the week:', en_weekdays[i.weekday()])
            print('Start time:', start_time)
            print('End time:', end_time)
            print('Type of class: ', class_type)
            print('Room:', location)
            print('Lecturer: ', lecturer, '\n')

            if i.weekday() == 0:
                week_num += 1
        i += timedelta(days=1)

# retrieves current date/time
# today = datetime.today()
# print(datetime.weekday(today))

# test
# myterm = set_term()
# divide_by_weeks(myterm)
