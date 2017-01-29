import csv
import os
import time_keeper

os.chdir(".")


def parse_file(filename):
    while True:
            try:
                if os.path.exists(filename) & filename.endswith('.csv'):
                    print('Opening file: ' + filename + '\n')
                    csv_file = open_file(filename)
                    return csv_file
                else:
                    raise FileNotFoundError
            except FileNotFoundError:
                filename = input('Give a proper file name\n')
            except Exception:
                print('Oops, something unpredictable went wrong!')
                break


def open_file(filename):
    rows = []
    with open(filename, 'rt', encoding='windows 1250') as csv_input:
        reader = csv.reader(csv_input, delimiter=';')

        for row in reader:
            rows.append(row)
    return rows

# help functions
# add a function below to check if the content of file is in proper format!


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


# temp block
def get_week_day(week_day):
    if week_day == 'Pn':
        week_day_input = 16
    elif week_day == 'Wt':
        week_day_input = 17
    elif week_day == 'Śr':
        week_day_input = 18
    elif week_day == 'Czw':
        week_day_input = 19
    else:
        week_day_input = 20
    return week_day_input


def add_to_existing_ics(filename, class_title, week_day, start_time, end_time, weeks, class_type, location, lecturer):
    output_file = open(filename, 'a')

    # start_time = start_time[0:2] + start_time[3:]
    # end_time = end_time[0:2] + end_time[3:]

    # temp
    week_day_input = get_week_day(week_day)

    output_file.write('BEGIN:VEVENT\n')
    output_file.write('DTSTART:201701' + str(week_day_input) + 'T' + start_time + '00Z\n')
    output_file.write('DTEND:201701' + str(week_day_input) + 'T' + end_time + '00Z\n')
    # output_file.write('RRULE:FREQ=WEEKLY;UNTIL=20170217T000000Z\n')
    output_file.write('SUMMARY:' + class_title + '\n')
    output_file.write('DESCRIPTION: Prowadzący: ' + lecturer + '\n')
    output_file.write('LOCATION:' + location + '\n')
    output_file.write('TRANSP:OPAQUE\n')
    output_file.write('END:VEVENT\n\n')

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
    class_type = gathered_data[4]
    location = gathered_data[5]
    lecturer = gathered_data[6]

    i = term_start
    week_num = 0

    while i <= term_end:

        if i == holidays_start:
            week_num += 1
            print('Holidays\n')
            # print('Week', week_num)
            i = holidays_end + time_keeper.timedelta(days=1)
            continue

        if i.weekday() == 0:
            week_num += 1

        if i.weekday() == week_day_index:
            print('BEGIN:VEVENT')
            print('DTSTART:' + i.strftime('%Y%m%d') + 'T' + start_time + '00Z')
            print('DTEND:' + i.strftime('%Y%m%d') + 'T' + end_time + '00Z')
            # output_file.write('RRULE:FREQ=WEEKLY;UNTIL=20170217T000000Z\n')
            print('SUMMARY:' + class_title)
            print('DESCRIPTION:Prowadzący: ' + lecturer)
            print('LOCATION:' + location)
            print('TRANSP:OPAQUE')
            print('END:VEVENT\n')

            # print('Week', week_num)
            # print('Class:', class_title)
            # print(i.strftime('%Y%m%d'), 'Day of the week:', i.weekday())
            # print('Start time:', start_time)
            # print('End time:', end_time)
            # print('Type of class: ', class_type)
            # print('Room:', location)
            # print('Lecturer: ', lecturer, '\n')
        i += time_keeper.timedelta(days=1)

