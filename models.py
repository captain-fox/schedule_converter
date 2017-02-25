import csv
import sys


class Event:

    TIME_ZONE = 'Europe/Warsaw'

    def __init__(self, row):

        self.class_title = row[Group.get_group_column()]
        self.week_day = ''
        self.start_time = ''
        self.end_time = ''
        self.weeks = ''
        self.class_type = ''
        self.location = ''
        self.lecturer = ''

    # test method
    def simulate_ics_output(self, day):

        print('BEGIN:VEVENT')
        print('DTSTART;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00')
        print('DTEND;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00')
        print('SUMMARY:' + self.class_title)
        print('DESCRIPTION: Prowadzący: ' + self.lecturer)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')


class FileWriter:

    @staticmethod
    def read_csv_file(filename):

        csv_rows = []
        try:
            with open(filename, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                for row in reader:
                    csv_rows.append(row)
            print('Working on file: ' + filename + '\n')
            return csv_rows
        except FileNotFoundError:
            print('File you\'re trying to read does not exist.')
            sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            sys.exit(0)
        except Exception as ex:
            print('Unexpected type of exception: "', ex, '" occurred in read_csv_file method.')
            sys.exit(0)

    @staticmethod
    def create_and_prepare_file(grouptitle):

        filename = (grouptitle + '.ics')
        try:
            newfile = open(filename, 'w')
            newfile.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n\n')
            newfile.close()
            return filename
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
    def append_to_ics(event, file_name, day):

        output_file = open(file_name, 'a')
        output_file.write('BEGIN:VEVENT\n')
        output_file.write('DTSTART;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.start_time + '00\n')
        output_file.write('DTEND;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.end_time + '00\n')
        output_file.write('SUMMARY:' + event.class_title + '\n')
        output_file.write('DESCRIPTION: Prowadzący: ' + event.lecturer + '\n')
        output_file.write('LOCATION:' + event.location + '\n')
        output_file.write('TRANSP:OPAQUE\n')
        output_file.write('END:VEVENT\n\n')
        output_file.close()

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

    __HEADERS__ = {
        'Day': '',
        'Time': '',
        'Weeks': '',
        'EventCat': '',
        'Module': '',
        'Room': '',
        'Surname': '',
        'Group': '',
    }

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
            # Kicking out empty space '' from set.
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

    @staticmethod
    def get_day_column():
        return Group.__HEADERS__['Day']

    @staticmethod
    def get_time_column():
        return Group.__HEADERS__['Time']

    @staticmethod
    def get_weeks_column():
        return Group.__HEADERS__['Weeks']

    @staticmethod
    def get_class_column():
        return Group.__HEADERS__['EventCat']

    @staticmethod
    def get_module_column():
        return Group.__HEADERS__['Module']

    @staticmethod
    def get_room_column():
        return Group.__HEADERS__['Room']

    @staticmethod
    def get_teacher_column():
        return Group.__HEADERS__['Surname']

    @staticmethod
    def get_group_column():
        return Group.__HEADERS__['Group']

