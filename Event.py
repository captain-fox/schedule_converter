from InputConverter import *
from FileHandler import *
from abc import abstractmethod, ABCMeta


class Event:

    TIME_ZONE = 'Europe/Warsaw'
    EVENTS = []

    def __init__(self, row):

        self.class_title = InputConverter.get_class_title_from(row)
        self.week_day = InputConverter.get_week_day_from(row)
        self.start_time = InputConverter.get_start_time_from(row)
        self.end_time = InputConverter.get_end_time_from(row)
        self.weeks = ''
        self.class_type = InputConverter.get_class_type_from(row)
        self.location = InputConverter.get_location_from(row)
        self.teacher = InputConverter.get_teacher_from(row)

    @staticmethod
    def collect_events_for_group(schedule, group):
        try:
            for _class in schedule[:len(schedule)-1]:
                if _class[InputConverter.group_column()] == group:
                    if _class[InputConverter.class_title_column()] == '':
                        continue
                    else:
                        Event.EVENTS.append(Event(_class))
        except Exception as e:
            print('Unpredicted exception while collecting events: {}'.format(e))


