import csv
import file_loader, group_info, get_groups

filename = file_loader.file_loader()

lines = []
groups = []



with open(filename, 'rt', encoding='windows 1250') as fileinput:

    reader = csv.reader(fileinput, delimiter=';')

    for row in reader:
        lines.append(row)

    #filling up the list of groups
groups = get_groups.get_groups(groups, lines)

    # Just to make sure there's something in 'groups'
    # print(groups[1:])

    # user_choice = input('Group?')

    # setting up user_choice to make things simpler for testing
user_choice = '5I'
group_info.collect_group_info(lines, user_choice)



