import csv

with open('plan.csv', 'rt', encoding='windows 1250') as fileinput:

    reader = csv.reader(fileinput, delimiter=';')

    # rows = []
    # for row in reader:
    #     rows.append(row)
    # creating a list of groups
    groups = []
    #filling up the list of groups
    for row in reader:
        if row[12] in groups:
            continue
        elif row[12] is '':
            continue
        else:
            groups.append(row[12])

    # Just to make sure there's something in 'groups'
    print(groups[1:])

    # user_choice = input('Group?')

    # setting up user_choice to make things simpler for testing
    user_choice = '5I IO2'

    fileinput.seek(0)

    reader = csv.reader(fileinput, delimiter=';')
    for row in reader:
        if row[12] == user_choice:
            print(row)


