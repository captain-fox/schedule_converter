from Event import *
from TermHandler import *
from _datetime import *
from InputConverter import *
from Group import *
from OutputHandler import *


# Facade between GUI and back-end
def facade():

    filename = '17l.txt'
    schedule = FileHandler.read_csv_file(filename, InputConverter.__HEADERS__)

    term = SummerTerm(date(2017, 2, 27), date(2017, 6, 21), date(2017, 4, 14), date(2017, 4, 18))

    groups = Group.get_groups(schedule)
    print(groups)

    db = Event.collect_events_for_group(schedule, '6I IO-2')

    # FileCreator.create_ics(group, term)
    # ConsoleLogger.create_ics(group, term)

    outputfile = None
    # outputfile = FileHandler.create_and_prepare_file('6I IO-2')
    for e in db:
        FileHandler.add_to_existing_ics(e, term, outputfile)
    # FileHandler.finalise_file(outputfile)

if __name__ == '__main__':
    facade()
