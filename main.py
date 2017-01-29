import csv
import file_manager
import group_manager
import time_keeper

# filename = input('Paste name of a file to process\n')
filename = 'plan.csv'
rows = file_manager.parse_file(filename)


#creating the list of groups
groups = group_manager.get_groups(rows)
print(groups[1:])
# weeks = group_info.get_weeks(lines)
# print(weeks)

# term
term = time_keeper.set_term()
time_keeper.show_term_info(term[0], term[1], term[2], term[3])


# user_choice = input('Group?')
# setting up user_choice to make things simpler for testing
# user_group = '5I'
user_group = '5I IO2'
group_manager.collect_group_info(rows, user_group, term)
# group_info.parse_data_to_ics(lines, user_group)

