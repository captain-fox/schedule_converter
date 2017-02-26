import csv
import sys


class Event:

    TIME_ZONE = 'Europe/Warsaw'

    def __init__(self, row):

        self.class_title = InputConverter.get_class_title_from(row)
        self.week_day = ''
        self.start_time = ''
        self.end_time = ''
        self.weeks = ''
        self.class_type = ''
        self.location = ''
        self.teacher = ''

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
        print('DESCRIPTION: Prowadzący: ' + self.teacher)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')


class FileHandler:

    @staticmethod
    def read_csv_file(file_name):

        csv_rows = []
        try:
            with open(file_name, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                for row in reader:
                    csv_rows.append(row)
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
    def finalise_file(file_name):

        output_file = open(file_name, 'a')
        output_file.write('END:VCALENDAR')
        output_file.close()

    @staticmethod
    def add_to_existing_ics(file_name, event):
        if isinstance(event, Event):
            output_file = open(file_name, 'a')
            print('Further implementation...')

            output_file.close()


class Group:

    @staticmethod
    def get_groups(rows):
        counter = 1

        try:
            number_of_rows = sum(1 for row in rows[1:])
            #using set to store unique values only
            groups = set([])

            while counter < number_of_rows:
                groups.add(rows[counter][12])
                counter += 1
            # Kicking out empty space element from groups
            if '' in groups:
                groups.remove('')

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
        'Day': '',
        'Time': '',
        'Weeks': '',
        'EventCat': '',
        'Module': '',
        'Room': '',
        'Surname': '',
        'Group': ''
    }

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
        return InputConverter.__HEADERS__['EventCat']

    @staticmethod
    def module_column():
        return InputConverter.__HEADERS__['Module']

    @staticmethod
    def room_column():
        return InputConverter.__HEADERS__['Room']

    @staticmethod
    def teacher_column():
        return InputConverter.__HEADERS__['Surname']

    @staticmethod
    def group_column():
        return InputConverter.__HEADERS__['Group']

    @staticmethod
    def get_class_title_from(row):
        return row[InputConverter.teacher_column()]

    @staticmethod
    def get_week_day_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_start_time_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_end_time_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_weeks_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_class_type_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_location_from(row):
        # implementation...
        return 0

    @staticmethod
    def get_teacher_from(row):
        # implementation...
        return 0