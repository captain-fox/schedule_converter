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


def collect_group_info(lines, user_course, user_group):
    for row in lines:
        if row[12] == user_course or row[12] == user_group:
            if row[6] == '':
                continue
            else:
                print("Class: " + row[6])
                print("Day of the week: " + row[1])
                print("Time: " + row[2])
                print("Weeks: " + row[3])
                print("Type of class: " + row[4])
                print("Room: " + row[8])
                print("Lecturer: " + row[9] + "\n")

