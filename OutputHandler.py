from abc import abstractmethod, ABCMeta


class ICSFormatter(ABCMeta):

    @staticmethod
    @abstractmethod
    def create_ics(event, day, filename=None): pass


class FileCreator(ICSFormatter):

    @staticmethod
    def create_ics(event, day, file_name=None):
        pass


class ConsoleLogger(ICSFormatter):

    @staticmethod
    def create_ics(event, day, file_name=None):
        pass