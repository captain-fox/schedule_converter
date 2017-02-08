import file_manager
import group_manager
import time_keeper

# Opening a proper csv ––––––––––––––––––––––––––––––––––––––––––––––––––––
# filename = input('Paste name of a file to process\n')
filename = 'schedule.csv'
rows = file_manager.parse_file(filename)


# Creating list of groups –––––––––––––––––––––––––––––––––––––––––––––––––
groups = group_manager.get_groups(rows)
# print(groups[1:])
# weeks = group_info.get_weeks(lines)
# print(weeks)

# Sets term and holidays break
term = time_keeper.set_term()
# time_keeper.show_term_info(term)




# Collecting data for a certain group –––––––––––––––––––––––––––––––––––––
# user_choice = input('Group?')
# setting up user_choice to make things simpler for testing
# user_group = '5I'
user_group = '5I IO2'


# Preview (does not create a file) ––––––––––––––––––––––––––––––––––––––––
# group_manager.collect_group_info(rows, user_group, term)
group_manager.preview_events(rows, user_group)


# Creates calendar file –––––––––––––––––––––––––––––––––––––––––––––––––––
# group_manager.parse_data_to_ics(rows, user_group, term)

