import csv
import file_manager
import group_info

# filename = input('Paste name of a file to process\n')
filename = 'plan.csv'
lines = []
groups = []
lines = file_manager.parse_file(filename)


#creating the list of groups
groups = group_info.get_groups(lines)

print(groups[1:])

# user_choice = input('Group?')
# setting up user_choice to make things simpler for testing
# user_course = '5I'
user_group = '5I IO2'
group_info.collect_group_info(lines, user_group)
# group_info.parse_data_to_ics(lines, user_group)

