from model import *
from term import *
from _datetime import *


# Facade between GUI and back-end

filename = '17l.txt'
schedule = FileHandler.read_csv_file(filename, InputConverter.__HEADERS__)
term1 = SummerTerm(date(2016, 9, 26), date(2017, 1, 25), date(2016, 12, 22), date(2017, 1, 2))
print(term1.return_term_start())
term2 = WinterTerm(date(2016, 9, 26), date(2017, 1, 25), date(2016, 12, 22), date(2017, 1, 2))

groups = Group.get_groups(schedule)
# print(groups)

d = date(2017, 1, 2)
gr = '6I IO-2'
objects = []

# Event.collect_events_for_group(schedule, gr)

# for e in Event.EVENTS:
#     e.preview_ics_output(d)
#     print()
