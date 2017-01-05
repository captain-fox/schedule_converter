import csv
import file_manager, group_info, get_groups

filename = file_manager.search_for_file()
lines = []
groups = []

with open(filename, 'rt', encoding='windows 1250') as csv_input:

    reader = csv.reader(csv_input, delimiter=';')

    for row in reader:
        lines.append(row)

#filling up the list of groups
groups = group_info.get_groups(groups, lines)

# print(groups[1:])

# user_choice = input('Group?')

# setting up user_choice to make things simpler for testing
user_choice = '5I'
group_info.collect_group_info(lines, user_choice)



