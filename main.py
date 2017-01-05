import csv
import file_finder

filename = file_finder.file_finder()

lines = []
groups = []



with open(filename, 'rt', encoding='windows 1250') as fileinput:

    reader = csv.reader(fileinput, delimiter=';')

    for row in reader:
        lines.append(row)

    #filling up the list of groups
    for row in lines:
        if row[12] in groups:
            continue
        elif row[12] is '':
            continue
        else:
            groups.append(row[12])

    # Just to make sure there's something in 'groups'
    # print(groups[1:])

    # user_choice = input('Group?')

    # setting up user_choice to make things simpler for testing
    user_choice = '5I'

    for row in lines:
        if row[12] == user_choice:
            print(row)


