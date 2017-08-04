from Event import *
from TermHandler import *
from _datetime import *
from InputConverter import *
from Group import *
from OutputHandler import *
from FileHandler import *
from DatabaseHandler import *


class DatabaseBridge:

    def __init__(self):
        self.raw_schedule = []
        self.processed_schedule = []
        self.winter_term = object
        # self.summer_term = SummerTerm(date(2017, 2, 27), date(2017, 6, 21), date(2017, 4, 14), date(2017, 4, 18))
        # self.groups_table = Group.get_groups(self.raw_schedule)

    #     TODO: implement connection to db

    def import_ics(self, file_name):
        self.raw_schedule = FileHandler.read_csv_file(file_name, InputConverter.__HEADERS__)


