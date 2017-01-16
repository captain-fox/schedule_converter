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
    print("Class: " + class_title)
    print("Day of the week: " + week_day)
    print("Start time: " + start_time)
    print("End time: " + end_time)
    print("Weeks: " + weeks)
    print("Type of class: " + class_type)
    print("Room: " + location)
    print("Lecturer: " + lecturer + "\n")


