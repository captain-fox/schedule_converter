from Event import *
from TermHandler import *
from _datetime import *
from InputConverter import *
from Group import *
from OutputHandler import *
from FileHandler import *
from DatabaseHandler import *


# Facade between GUI and back-end
def facade():

    filename = '17l.txt'
    schedule = FileHandler.read_csv_file(filename, InputConverter.__HEADERS__)

    term = SummerTerm(date(2017, 2, 27), date(2017, 6, 21), date(2017, 4, 14), date(2017, 4, 18))
    groups = Group.get_groups(schedule)
    print(groups)
    # db = Event.collect_events_for_group(schedule, '6I bl ISA')
    # db = Event.collect_events_for_group(schedule, '6I')
    db = Event.collect_events_for_group(schedule, '6I IO-2')

    # # #

    drb = DatabaseBridge()
    drb.import_ics('17l.txt')

    # # #

    # outputfile = '6I bl ISA'
    # outputfile = '6I IO-2'
    # outputfile = '6I bl TMB'
    # outputfile = '6I'
    outputfile = None
    if outputfile is None:
        strategy = ConsoleLogger.create_ics
        outputfile = sys.stdout
        FileHandler.add_to_existing_ics(strategy, db, term, outputfile)
    else:
        strategy = FileCreator.create_ics
        outputfile = FileHandler.create_and_prepare_file(outputfile)
        FileHandler.add_to_existing_ics(strategy, db, term, outputfile)
        FileHandler.finalise_file(outputfile)


if __name__ == '__main__':
    facade()
