import csv
import calendar

calendar.setfirstweekday(calendar.MONDAY)
import file_manager, group_info

filename = file_manager.search_for_file()
lines = []
groups = []

with open(filename, 'rt', encoding='windows 1250') as csv_input:

    reader = csv.reader(csv_input, delimiter=';')

    for row in reader:
        lines.append(row)

#filling up the list of groups
groups = group_info.get_groups(lines)

print(groups[1:])

# user_choice = input('Group?')

# setting up user_choice to make things simpler for testing
# user_course = '5I'
user_group = '5I IO2'
group_info.collect_group_info(lines, user_group)

