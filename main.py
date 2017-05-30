from Event import *
from TermHandler import *
from _datetime import *


# Facade between GUI and back-end

filename = '17l.txt'
schedule = FileHandler.read_csv_file(filename, InputConverter.__HEADERS__)

sterm = SummerTerm(date(2017, 2, 27), date(2017, 6, 21), date(2017, 4, 14), date(2017, 4, 18))
sterm.display_term()

groups = Group.get_groups(schedule)
print(groups)

d = date(2017, 1, 2)
gr = '6I IO-2'
objects = []

Event.collect_events_for_group(schedule, gr)

for e in Event.EVENTS:
    e.preview_ics_output(d)
    print()
