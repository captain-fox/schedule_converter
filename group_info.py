import file_manager

def get_groups(lines):
    groups = []
    for row in lines:
        if row[12] in groups:
            continue
        elif row[12] is '':
            continue
        else:
            groups.append(row[12])
    return sorted(groups)


def collect_group_info(lines, user_group):
    for row in lines:
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
                # file_manager.add_to_ics(class_title,week_day, start_time, end_time, weeks, class_type, location, lecturer)


