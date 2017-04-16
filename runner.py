import model
from _datetime import *

filename = '17l.txt'
rows = model.FileHandler.read_csv_file(filename)
model.InputConverter.set_term(date(2016, 9, 26), date(2017, 1, 25), date(2016, 12, 22), date(2017, 1, 2))
groups = model.Group.get_groups(rows)
print(groups)

d = date(2017, 1, 2)
gr = '6I IO-2'
objects = []

model.Event.collect_events_for_group(rows, gr)

for e in model.Event.EVENTS:
    e.preview_ics_output(d)
    print()
