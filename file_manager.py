import glob
import os

os.chdir(".")


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


def add_to_ics(class_title,week_day, start_time, end_time, weeks, class_type, location, lecturer):
    output_file = open('schedule.ics', 'w')
    output_file.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nBEGIN:VEVENT\nDTSTART:20170117T080000Z\nDTEND:20170117T090000Z\nRRULE:FREQ=WEEKLY;UNTIL=20170217T000000Z\nSUMMARY:Event title\nLOCATION:i24 E107\nTRANSP:OPAQUE\nEND:VEVENT\nEND:VCALENDAR')
    output_file.close()



