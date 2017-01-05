def get_groups(groups, lines):
    for row in lines:
        if row[12] in groups:
            continue
        elif row[12] is '':
            continue
        else:
            groups.append(row[12])
    return groups


def collect_group_info(lines, user_choice):
    for row in lines:
        if row[12] == user_choice:
            print(row)