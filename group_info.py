def collect_group_info(lines, user_choice):
    for row in lines:
        if row[12] == user_choice:
            print(row)