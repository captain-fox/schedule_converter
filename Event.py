from InputConverter import *
from FileHandler import *
import sys


class Event:

    TIME_ZONE = 'Europe/Warsaw'
    # EVENTS = []

    def __init__(self, row):

        self.class_title = InputConverter.get_class_title_from(row)
        self.week_day = InputConverter.get_week_day_from(row)
        self.start_time = InputConverter.get_start_time_from(row)
        self.end_time = InputConverter.get_end_time_from(row)
        self.weeks = InputConverter.get_weeks_from(row)
        self.class_type = InputConverter.get_class_type_from(row)
        self.location = InputConverter.get_location_from(row)
        self.teacher = InputConverter.get_teacher_from(row)

    @staticmethod
    def collect_events_for_group(schedule, group):
        try:
            class_set = []
            for _class in schedule[:len(schedule)-1]:
                if (_class[InputConverter.group_column()] == group) and (_class[InputConverter.class_title_column()] != ''):
                    class_set.append(Event(_class))
                    # Event.EVENTS.append(Event(_class))

            return class_set
        except Exception as e:
            print('Unpredicted exception while collecting events: {}'.format(e))


