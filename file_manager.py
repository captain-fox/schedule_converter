import csv
import glob
import os

os.chdir(".")

def parse_file(filename):
    while True:
            try:
                if os.path.exists(filename) & filename.endswith('.csv'):
                    print('Opening file: ' + filename + '\n')
                    return filename
                    break
                else:
                    raise FileNotFoundError

            except FileNotFoundError:
                print('No finde por favor!\n')
                filename = input('Give a proper file name\n')





def search_for_file():
    n = 0
    for file in glob.glob("*.csv"):

        n += 1

        if n > 1:
            print("More than one .csv file found")
            for filelist in glob.glob("*.csv"):
                print(filelist)
        elif n < 1:
            print("No .csv files found in directory")
            for filelist in glob.glob("*.csv"):
                print(filelist)

    print("File found: " + file + "\n")
    return file


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



def add_to_existing_ics(filename, class_title,week_day, start_time, end_time, weeks, class_type, location, lecturer):
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



