import csv
import os
import time_keeper
import group_manager

os.chdir(".")


def open_file(filename):
    rows = []
    with open(filename, 'rt', encoding='windows 1250') as csv_input:
        reader = csv.reader(csv_input, delimiter=';')

        for row in reader:
            rows.append(row)
    return rows


def parse_file(filename):
    while True:
            try:
                if os.path.exists(filename) & filename.endswith('.csv'):
                    print('Working on file: ' + filename + '\n')
                    rows = open_file(filename)
                    check_header(rows[0])
                    return rows
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                filename = input('Give a proper file name\n')
            except Exception:
                print('Oops, headers don\'t match!')
                break


def check_header(header_row):
    for columnHeader in header_row:
        if columnHeader in group_manager.__headers__:
            group_manager.__headers__[columnHeader] = header_row.index(columnHeader)
    for value in group_manager.__headers__.values():
        if value is '':
            raise Exception
    # print(__headers__)


def create_and_prepare_empty_file(grouptitle):
    filename = (grouptitle + '.ics')
    newfile = open(filename, 'w')
    newfile.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n\n')
    newfile.close()
    return filename


def finalise_file(filename):
    filename = open(filename, 'a')
    filename.write('END:VCALENDAR')
    filename.close()


def add_to_existing_ics(filename, term, gathered_data):
    output_file = open(filename, 'a')

    term_start = term[0]
    term_end = term[1]
    holidays_start = term[2]
    holidays_end = term[3]

    class_title = gathered_data[0]
    week_day_index = gathered_data[1]
    start_time = gathered_data[2]
    end_time = gathered_data[3]
    # class_type = gathered_data[4]
    location = gathered_data[5]
    lecturer = gathered_data[6]

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == holidays_start:
            week_num += 1
            i = holidays_end + time_keeper.timedelta(days=1)
            continue

        if i.weekday() == 0:
            week_num += 1

        if i.weekday() == week_day_index:

            output_file.write('BEGIN:VEVENT\n')
            output_file.write('DTSTART;TZID=Europe/Warsaw:' + i.strftime('%Y%m%d') + 'T' + start_time + '00\n')
            output_file.write('DTEND;TZID=Europe/Warsaw:' + i.strftime('%Y%m%d') + 'T' + end_time + '00\n')
            output_file.write('SUMMARY:' + class_title + '\n')
            output_file.write('DESCRIPTION: Prowadzący: ' + lecturer + '\n')
            output_file.write('LOCATION:' + location + '\n')
            output_file.write('TRANSP:OPAQUE\n')
            output_file.write('END:VEVENT\n\n')

        i += time_keeper.timedelta(days=1)

    output_file.close()


def preview_ics_output(term, gathered_data):

    term_start = term[0]
    term_end = term[1]
    holidays_start = term[2]
    holidays_end = term[3]

    class_title = gathered_data[0]
    week_day_index = gathered_data[1]
    start_time = gathered_data[2]
    end_time = gathered_data[3]
    # class_type = gathered_data[4]
    location = gathered_data[5]
    lecturer = gathered_data[6]

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == holidays_start:
            week_num += 1
            # print('Holidays\n')
            # print('Week', week_num)
            i = holidays_end + time_keeper.timedelta(days=1)
            continue

        if i.weekday() == 0:
            week_num += 1

        if i.weekday() == week_day_index:
            print('BEGIN:VEVENT')
            print('DTSTART:' + i.strftime('%Y%m%d') + 'T' + start_time + '00')
            print('DTEND:' + i.strftime('%Y%m%d') + 'T' + end_time + '00')
            # output_file.write('RRULE:FREQ=WEEKLY;UNTIL=20170217T000000Z\n')
            print('SUMMARY:' + class_title)
            print('DESCRIPTION:Prowadzący: ' + lecturer)
            print('LOCATION:' + location)
            print('TRANSP:OPAQUE')
            print('END:VEVENT\n')

        i += time_keeper.timedelta(days=1)
