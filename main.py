import csv
import file_manager
import group_manager

# filename = input('Paste name of a file to process\n')
filename = 'plan.csv'
rows = file_manager.parse_file(filename)


#creating the list of groups
groups = group_manager.get_groups(rows)
# weeks = group_info.get_weeks(lines)

print(groups[1:])
# print(weeks)

# user_choice = input('Group?')
# setting up user_choice to make things simpler for testing
# user_group = '5I'
user_group = '5I IO2'
group_manager.collect_group_info(rows, user_group)
# group_info.parse_data_to_ics(lines, user_group)

