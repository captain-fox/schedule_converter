class Term:

    __instantiated = False

    def __init__(self, term_start, term_end, holidays_start, holidays_end, day_offs=None):

        if not self.instantiated():

            self.instantiate()
            self.term_start = term_start
            self.term_end = term_end
            self.holidays_start = holidays_start
            self.holidays_end = holidays_end
            self.day_offs = day_offs
            self.observers = []

        else:
            print('Updating...')
            self.update_term(term_start, term_end, holidays_start, holidays_end)
            # self.notify_observers()

    @classmethod
    def instantiated(cls):
        return cls.__instantiated

    @classmethod
    def instantiate(cls):
        # print('Instantiating ' + str(cls))
        cls.__instantiated = True

    def add_observer(self, observer):
        self.observers.append(observer)

    def push_update(self):
        for observer in self.observers:
            observer.update()

    def update_term(self, term_start, term_end, holidays_start, holidays_end, day_offs=None):
        # TODO: Loop through db and update records that have changed.
        # for arg in args:
            # TODO: strategy design pattern method for field update instead.
        # print('Implementation...')
        self.term_start = term_start
        self.term_end = term_end
        self.holidays_start = holidays_start
        self.holidays_end = holidays_end
        self.day_offs = day_offs

    def display_term(self):
        print('Semester starts: {}\nSemester ends: {}\nHolidays start: {}\nHolidays end: {}'
              .format(self.term_start, self.term_end, self.holidays_start, self.holidays_end))

    def return_term_start(self):
        return self.term_start

    def return_term_end(self):
        return self.term_end

    def return_holidays_start(self):
        return self.holidays_start

    def return_holidays_end(self):
        return self.holidays_end

    def return_day_offs(self):
        return self.day_offs

    # def make(self, day_from, day_to):
    #     day_from = day_to
    #
    # def __call__(self, *args, **kwargs):
    #     print('Call method ran')


class SummerTerm(Term):
    pass


class WinterTerm(Term):
    pass


