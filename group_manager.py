import file_manager


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


def parse_data_to_ics(rows, grouptitle):
    filename = file_manager.create_and_prepare_empty_file(grouptitle)
    for row in rows:
        if row[12] == grouptitle:
            # Doesn't parse events with empty 'Module' field
            if row[6] == '':
                continue
            else:
                class_title = row[6]
                week_day = row[1]
                # converting start/end time into "hhmm" format for .ics
                start_time = row[2][0:2] + row[2][3:5]
                end_time = row[2][6:8] + row[2][9:]
                weeks = row[3]
                class_type = row[4]
                location = row[8]
                lecturer = row[9]
                file_manager.add_to_existing_ics(filename, class_title, week_day, start_time, end_time, weeks, class_type, location, lecturer)
    file_manager.finalise_file(filename)


def collect_group_info(rows, user_group):
    for row in rows:
        if row[12] == user_group:
            # Doesn't print events with empty 'Module' field
            if row[6] == '':
                continue
            else:
                class_title = row[6]
                week_day = row[1]
                start_time = row[2][0:5]
                end_time = row[2][6:]
                weeks = row[3]
                class_type = row[4]
                location = row[8]
                lecturer = row[9]
                print("Class: " + class_title)
                print("Day of the week: " + week_day)
                print("Start time: " + start_time)
                print("End time: " + end_time)
                print("Weeks: " + weeks)
                print("Type of class: " + class_type)
                print("Room: " + location)
                print("Lecturer: " + lecturer + "\n")

