from Event import *
from TermHandler import *
from _datetime import *
from InputConverter import *
from Group import *


# TODO: Facade between GUI and back-end
def main():

    filename = '17l.txt'
    schedule = FileHandler.read_csv_file(filename, InputConverter.__HEADERS__)

    term = SummerTerm(date(2017, 2, 27), date(2017, 6, 21), date(2017, 4, 14), date(2017, 4, 18))
    term.display_term()

    groups = Group.get_groups(schedule)
    print(groups)

    Event.collect_events_for_group(schedule, '6I IO-2')

    outputfile = None
    # outputfile = FileHandler.create_and_prepare_file('6I IO-2')
    outputfile = '6I IO-2'
    for e in Event.EVENTS:
        FileHandler.process_event(e, term, outputfile)
        # e.preview_ics_output(d)
        print()

if __name__ == '__main__':
    main()
