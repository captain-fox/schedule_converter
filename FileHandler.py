import csv
from InputConverter import *


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
