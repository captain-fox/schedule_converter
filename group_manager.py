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
    for row in rows:
        if row[12] in groups:
            continue
        elif row[12] is '':
            continue
        else:
            groups.append(row[12])
    return sorted(groups)


def get_weeks(rows):
    weeks = []
    for row in rows:
        if row[3] in weeks:
            continue
        elif row[3] is '':
            continue
        else:
            weeks.append(row[3])
    return sorted(weeks)

# def get_event_repeat(weeks):


def create_calendar_for(rows, user_group, term):
    filename = file_manager.create_and_prepare_empty_file(user_group)
    for row in rows:
        if row[12] == user_group:
            # Doesn't print events with empty 'Module' field
            if row[6] == '':
                continue
            else:
                class_title = row[6]
                week_day_index = time_keeper.get_week_day_index(row[1])
                start_time = row[2][0:2] + row[2][3:5]
                end_time = row[2][6:8] + row[2][9:]
                class_type = row[4]
                location = row[8]
                lecturer = row[9]

                gathered_data = [class_title, week_day_index, start_time, end_time, class_type, location, lecturer]
                file_manager.add_to_existing_ics(filename, term, gathered_data)
    file_manager.finalise_file(filename)


def collect_group_info(rows, user_group, term):
    for row in rows:
        if row[12] == user_group:
            # Doesn't print events with empty 'Module' field
            if row[6] == '':
                continue
            else:
                class_title = row[6]
                week_day_index = time_keeper.get_week_day_index(row[1])
                # start_time = row[2][0:5]
                # end_time = row[2][6:]
                start_time = row[2][0:2] + row[2][3:5]
                end_time = row[2][6:8] + row[2][9:]
                class_type = row[4]
                location = row[8]
                lecturer = row[9]

                gathered_data = [class_title, week_day_index, start_time, end_time, class_type, location, lecturer]
                file_manager.preview_ics_output(term, gathered_data)


# Help methods ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

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


def preview_events(rows, user_group):
    for row in rows:
        if row[12] == user_group:

            if row[6] == '':  # Doesn't print events with empty 'Module' field
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