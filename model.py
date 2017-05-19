import csv

from InputConverter import *


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
        output_file.write('DTSTART;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00\n')
        output_file.write('DTEND;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00\n')
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
        print('DESCRIPTION: Prowadzący: ' + self.teacher + '; Rodzaj zajęć:' + self.class_type)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')

    @staticmethod
    def collect_events_for_group(schedule, group):
        for _class in schedule[:len(schedule) - 1]:

            if _class[InputConverter.group_column()] == group:
                if _class[InputConverter.class_title_column()] == '':
                    continue
                else:
                    Event.EVENTS.append(Event(_class))


class FileHandler:

    @staticmethod
    def read_csv_file(file_name, headers_dictionary):

        csv_rows = []
        try:
            with open(file_name, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                for row in reader:
                    csv_rows.append(row)
                #     Checking headers
                InputConverter.check_header(csv_rows[0], headers_dictionary)
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
    def add_to_existing_ics(file_name, event, term):
        if isinstance(event, Event):
            output_file = open(file_name, 'a')

            # TODO mechanism of appending events to calendar

            # i = term[term_start]
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


class Term:

    TERM_CREATED = False

    def __init__(self, term_start, term_end, holidays_start, holidays_end, day_offs=None):

        if not self.TERM_CREATED:
            self.term_start = term_start
            self.term_end = term_end
            self.holidays_start = holidays_start
            self.holidays_end = holidays_end
            self.day_offs = day_offs
            self.TERM_CREATED = True
        else:
            self.update_term()


    def update_term(self):
        # TODO: Loop through db and update records that have changed.
        print('Implementation...')


    def return_term_start(self):
        return self.term_start

    def return_term_end(self):
        return self.term_end

    def return_holidays_start(self):
        return self.holidays_start

    def return_holidays_end(self):
        return self.holidays_end

    def return_day_offs(self):
        return self.day_offs

    # def make(self, day_from, day_to):
        # make monday friday


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


