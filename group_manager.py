import file_manager
import time_keeper

__headers__ = {
    'Ref': '',
    'Day': '',
    'Time': '',
    'Weeks': '',
    'EventCat': '',
    'Module': '',
    'Room': '',
    'Surname': '',
    'Group': '',
}


def get_groups(rows):
    groups = []
    for row in rows[1:]:
        if row[get_group_column()] in groups:
            continue
        elif row[get_group_column()] is '':
            continue
        else:
            groups.append(row[get_group_column()])
    return sorted(groups)


def create_calendar_for(rows, user_group, term):
    filename = file_manager.create_and_prepare_empty_file(user_group)
    for row in rows:
        if row[get_group_column()] == user_group:
            # Doesn't create events with empty 'Module' field
            if row[get_module_column()] == '':
                continue
            else:
                class_title = row[get_module_column()]
                week_day_index = time_keeper.get_week_day_index(row[get_day_column()])
                start_time = row[get_time_column()][0:2] + row[get_time_column()][3:5]
                end_time = row[get_time_column()][6:8] + row[get_time_column()][9:]
                class_type = row[get_class_column()]
                location = row[get_room_column()]
                lecturer = row[get_teacher_column()]

                gathered_data = [class_title, week_day_index, start_time, end_time, class_type, location, lecturer]
                file_manager.add_to_existing_ics(filename, term, gathered_data)
    file_manager.finalise_file(filename)


def get_day_column():
    return __headers__['Day']


def get_time_column():
    return __headers__['Time']


def get_weeks_column():
    return __headers__['Weeks']


def get_class_column():
    return __headers__['EventCat']


def get_module_column():
    return __headers__['Module']


def get_room_column():
    return __headers__['Room']


def get_teacher_column():
    return __headers__['Surname']


def get_group_column():
    return __headers__['Group']


# Not used during runtime, help methods for testing –––––––––––––––––––––––––––––––––––––––––––
def preview_output_file(rows, user_group, term):
    for row in rows:
        if row[get_group_column()] == user_group:
            # Doesn't print events with empty 'Module' field
            if row[get_module_column()] == '':
                continue
            else:
                class_title = row[get_module_column()]
                week_day_index = time_keeper.get_week_day_index(row[get_day_column()])
                start_time = row[get_time_column()][0:2] + row[get_time_column()][3:5]
                end_time = row[get_time_column()][6:8] + row[get_time_column()][9:]
                class_type = row[get_class_column()]
                location = row[get_room_column()]
                lecturer = row[get_teacher_column()]

                gathered_data = [class_title, week_day_index, start_time, end_time, class_type, location, lecturer]
                file_manager.preview_ics_output(term, gathered_data)


def preview_events(rows, user_group):
    for row in rows:
        if row[get_group_column()] == user_group:
            # Doesn't print events with empty 'Module' field
            if row[get_module_column()] == '':
                continue
            else:
                class_title = row[get_module_column()]
                week_day = row[get_day_column()]
                start_time = row[get_time_column()][0:5]
                end_time = row[get_time_column()][6:]
                # weeks = row[get_weeks_column()]
                class_type = row[get_class_column()]
                location = row[get_room_column()]
                lecturer = row[get_teacher_column()]

                print('Class:', class_title)
                print('Day of the week:', week_day)
                print('Start time:', start_time)
                print('End time:', end_time)
                print('Type of class: ', class_type)
                print('Room:', location)
                print('Lecturer: ', lecturer, '\n')


def get_weeks(rows):
    weeks = []
    for row in rows:
        if row[get_weeks_column()] in weeks:
            continue
        elif row[get_weeks_column()] is '':
            continue
        else:
            weeks.append(row[get_weeks_column()])
    return sorted(weeks)
