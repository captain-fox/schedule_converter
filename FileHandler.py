import csv
from Event import *
from InputConverter import *
from FormattingStrategy import *
from TermHandler import *
from _datetime import *


class FileHandler:

    @staticmethod
    def read_csv_file(file_name, headers_dictionary):

        # csv_rows = []
        try:
            with open(file_name, 'rt', encoding='windows 1250') as csv_input:
                reader = csv.reader(csv_input, delimiter=';')
                csv_rows = [row for row in reader]
                # for row in reader:
                #     csv_rows.append(row)
                #     Checking headers
                InputConverter.check_header(csv_rows[0], headers_dictionary)
            print('Working on file: {}\n'.format(file_name))

            return csv_rows

        except FileNotFoundError:
            print('File you\'re trying to read does not exist.')
            sys.exit(0)
        except UnicodeDecodeError:
            print('It\'s not even a text file!')
            sys.exit(0)
        except ValueError:
            print('Not all headers found')
        except Exception as e:
            print('Unexpected type of exception: "{}" occurred in read_csv_file method.'.format(e))
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
        except Exception as e:
            print('Unexpected type of exception: "{}" occurred in create_and_prepare_file method.'.format(e))
            sys.exit(0)

    @staticmethod
    def add_to_existing_ics(event, term, filename=None):

        processing_strategy = ICSFormatter.select_processing_method(filename)

        date_counter = term.term_start
        week_num = 0

        while date_counter <= term.term_end:

            if date_counter == term.holidays_start:
                print('\n\n\n Holidays!!! \n\n\n')
                week_num += 1
                date_counter = term.holidays_end + timedelta(days=1)
                continue

            if date_counter.weekday() == 0:
                # Switching weeks x1/x2
                week_num += 1

            if date_counter.weekday() == event.week_day:
                processing_strategy.pass_data(event, date_counter, filename)

            date_counter += timedelta(days=1)


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
