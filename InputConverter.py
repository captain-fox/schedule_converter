import sys


class InputConverter:

    __HEADERS__ = {
        'Day': '',  # weekday
        'Time': '',  # time event starts and ends
        'Weeks': '',  # numbers of weeks
        'EventCat': '',
        'Module': '',
        'Room': '',  # location
        'Surname': '',  # teacher
        'Group': ''  # id of group
    }

    pl_weekdays = ['Pn', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']
    # en_weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    @staticmethod
    def check_header(header_row, headers):
        for columnHeader in header_row:
            if columnHeader in headers:
                headers[columnHeader] = header_row.index(columnHeader)
        for value in headers.values():
            # show header and index ...
            if value is '':
                print('Header not found.')
                sys.exit(0)

    @staticmethod
    def get_week_day_index(week_day):
        d_index = InputConverter.pl_weekdays.index(week_day)
        return d_index

    # Getters of column indexes
    @staticmethod
    def day_column():
        return InputConverter.__HEADERS__['Day']

    @staticmethod
    def time_column():
        return InputConverter.__HEADERS__['Time']

    @staticmethod
    def weeks_column():
        return InputConverter.__HEADERS__['Weeks']

    @staticmethod
    def class_title_column():
        return InputConverter.__HEADERS__['Module']

    @staticmethod
    def event_cat_column():
        return InputConverter.__HEADERS__['EventCat']

    @staticmethod
    def room_column():
        return InputConverter.__HEADERS__['Room']

    @staticmethod
    def teacher_column():
        return InputConverter.__HEADERS__['Surname']

    @staticmethod
    def group_column():
        return InputConverter.__HEADERS__['Group']

# Collecting data for specific events
    @staticmethod
    def get_class_title_from(row):
        return row[InputConverter.class_title_column()]

    @staticmethod
    def get_week_day_from(row):  # returns index of a day!
        # natural_language_day = row[InputConverter.day_column()]
        d_index = InputConverter.get_week_day_index(row[InputConverter.day_column()])
        return d_index

    @staticmethod
    def get_start_time_from(row):
        # TODO: use .split('-') instead!
        start_time = row[InputConverter.time_column()][0:2] + row[InputConverter.time_column()][3:5]
        return start_time

    @staticmethod
    def get_end_time_from(row):
        end_time = row[InputConverter.time_column()][6:8] + row[InputConverter.time_column()][9:]
        return end_time

    @staticmethod
    def get_weeks_from(row):

        w = row[InputConverter.weeks_column()].split(',')
        # test input
        # w = ['1-5', '8', '9', '10-12', '14']
        weeks = []
        for item in w:

            if '-' in item:
                s = list(map(int, item.split('-')))
                s = [s for s in range(s[0], s[1] + 1)]
                weeks.extend(s)
            else:
                weeks.append(item)
        # print(weeks)
        return weeks

    @staticmethod
    def get_class_type_from(row):
        return row[InputConverter.event_cat_column()]

    @staticmethod
    def get_location_from(row):
        return row[InputConverter.room_column()]

    @staticmethod
    def get_teacher_from(row):
        return row[InputConverter.teacher_column()]
