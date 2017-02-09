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

# Collecting data for a certain group (from GUI)–––––––––––––––––––––––––––
# user_group = input('Group?')
# faculty_group = input('Lectures group?')
user_group = '5I IO2'
faculty_group = '5I'

# Preview (does not create a file) ––––––––––––––––––––––––––––––––––––––––
# group_manager.preview_output_file(rows, user_group, term)
# group_manager.preview_output_file(rows, faculty_group, term)
group_manager.preview_events(rows, user_group)
group_manager.preview_events(rows, faculty_group)

# Creates calendar file –––––––––––––––––––––––––––––––––––––––––––––––––––
# group_manager.create_calendar_for(rows, user_group, term)
# group_manager.create_calendar_for(rows, faculty_group, term)

