import csv
import sys
from _datetime import *


class Event:

    TIME_ZONE = 'Europe/Warsaw'
    EVENTS = []

    def __init__(self, row):

        self.class_title = InputConverter.get_class_title_from(row)
        self.week_day = InputConverter.get_week_day_from(row)
        self.start_time = InputConverter.get_start_time_from(row)
        self.end_time = InputConverter.get_end_time_from(row)
        self.weeks = ''
        self.class_type = InputConverter.get_class_type_from(row)
        self.location = InputConverter.get_location_from(row)
        self.teacher = InputConverter.get_teacher_from(row)

    def append_to_ics(self, file_name, day):

        output_file = open(file_name, 'a')
        output_file.write('BEGIN:VEVENT\n')
        output_file.write(
            'DTSTART;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00\n')
        output_file.write(
            'DTEND;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00\n')
        output_file.write('SUMMARY:' + self.class_title + '\n')
        output_file.write('DESCRIPTION: Prowadzący: ' + self.teacher + '\n')
        output_file.write('LOCATION:' + self.location + '\n')
        output_file.write('TRANSP:OPAQUE\n')
        output_file.write('END:VEVENT\n\n')
        output_file.close()

    # test method
    def preview_ics_output(self, day):

        print('BEGIN:VEVENT')
        print('DTSTART;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00')
        print('DTEND;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00')
        print('SUMMARY:' + self.class_title)
        print('DESCRIPTION: Prowadzący: ' + self.teacher + ' Zajęcia:' + self.class_type)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')

    @staticmethod
    def collect_events_for_group(rows, gr):
        for r in rows[:len(rows) - 1]:

            if r[InputConverter.group_column()] == gr:
                if r[InputConverter.class_title_column()] == '':
                    continue
                else:
                    Event.EVENTS.append(Event(r))


class FileHandler:

    @staticmethod
    # TODO: pass dictionary as argument
    def read_csv_file(file_name):

        csv_rows = []
        try:
            with open(file_name, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                for row in reader:
                    # TODO:
                    csv_rows.append(row)
                #     Checking headers
                # TODO: dictionary as argument
                InputConverter.check_header(csv_rows[0])
            print('Working on file: ' + file_name + '\n')

            return csv_rows

        except FileNotFoundError:
            print('File you\'re trying to read does not exist.')
            sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            sys.exit(0)
        except ValueError:
            print('Not all headers found')
        except Exception as ex:
            print('Unexpected type of exception: "', ex, '" occurred in read_csv_file method.')
            sys.exit(0)

    @staticmethod
    def create_and_prepare_file(group):

        file_name = (group + '.ics')
        try:
            newfile = open(file_name, 'w')
            newfile.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n\n')
            newfile.close()

            return file_name

        except FileNotFoundError:
            print('File does not exist.')
            sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            sys.exit(0)
        except Exception as ex:
            print('Unexpected type of exception: "', ex, '" occurred in create_and_prepare_file method.')
            sys.exit(0)

    @staticmethod
    def add_to_existing_ics(file_name, event):
        if isinstance(event, Event):
            output_file = open(file_name, 'a')

            # TODO mechanism of appending events to calendar

            # i = term_start
            # # week_num = 0
            #
            # while i <= term_end:
            #
            #     if i == holidays_start:
            #         # week_num += 1
            #         i = holidays_end + time_keeper.timedelta(days=1)
            #         continue
            #
            #     # if i.weekday() == 0:
            #     #     week_num += 1
            #
            #     if i.weekday() == week_day_index:
            # TODO list of events to iterate through, event as argument "e"
            #     Event.append_to_ics(e, file_name, i)
            #     i += time_keeper.timedelta(days=1)

            output_file.close()

    @staticmethod
    def finalise_file(file_name):

        output_file = open(file_name, 'a')
        output_file.write('END:VCALENDAR')
        output_file.close()

    @staticmethod
    def is_even_week(i):
        if i % 2 == 0:
            print('Week x2')
        else:
            print('Week x1')


class Group:

    @staticmethod
    def get_groups(rows):
        counter = 1

        try:
            # using set to store unique values only
            groups = set([])

            for row in rows[1:len(rows) - 1]:
                groups.add(row[InputConverter.group_column()])
                counter += 1
            # Kicking out empty space element from groups
            if '' in groups:
                groups.remove('')

            print(len(groups), 'unique groups found')
            return sorted(groups)

        except IndexError:
            print('Oops. Trying to read white spaces after table. IndexError in row:', counter)
            sys.exit(0)
        except TypeError:
            print('get_groups method in \'Groups\' tried to read non-existing file or file with unexpected structure.')
            sys.exit(0)
        except Exception as ex:
            print('Unexpected type of exception: "', ex, '" occurred in get_groups method.')
            sys.exit(0)


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

    rows = []

    pl_weekdays = ['Pn', 'Wt', 'Śr', 'Czw', 'Pt', 'Sb', 'Nd']
    # en_weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    @staticmethod
    def check_header(header_row):
        for columnHeader in header_row:
            if columnHeader in InputConverter.__HEADERS__:
                InputConverter.__HEADERS__[columnHeader] = header_row.index(columnHeader)
        for value in InputConverter.__HEADERS__.values():
            # show header and index ...
            if value is '':
                print('Header not found.')
                sys.exit(0)

    @staticmethod
    def get_week_day_index(week_day):
        d_index = InputConverter.pl_weekdays.index(week_day)
        return d_index

    @staticmethod
    def set_term(sem_start, sem_end, hol_start, hol_end):

        # term_start = date(2016, 9, 26)
        term_start = sem_start
        # term_end = date(2017, 1, 25)
        term_end = sem_end

        # holidays_start = date(2016, 12, 22)
        holidays_start = hol_start
        # holidays_end = date(2017, 1, 2)
        holidays_end = hol_end

        term = [term_start, term_end, holidays_start, holidays_end]

        return term

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
        start_time = row[InputConverter.time_column()][0:2] + row[InputConverter.time_column()][3:5]
        return start_time

    @staticmethod
    def get_end_time_from(row):
        end_time = row[InputConverter.time_column()][6:8] + row[InputConverter.time_column()][9:]
        return end_time

    @staticmethod
    def get_weeks_from(row):
        # TODO analyse weeks values
        return 0

    @staticmethod
    def get_class_type_from(row):
        return row[InputConverter.event_cat_column()]

    @staticmethod
    def get_location_from(row):
        return row[InputConverter.room_column()]

    @staticmethod
    def get_teacher_from(row):
        return row[InputConverter.teacher_column()]
