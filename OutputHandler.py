from abc import abstractmethod, ABCMeta


class ICSFormatter(ABCMeta):

    @staticmethod
    @abstractmethod
    def create_ics(event, day, filename=None):
        raise NotImplementedError('Can\'t call abstract method!')


class FileCreator(ICSFormatter):

    @staticmethod
    def create_ics(event, day, output=None):
        # create_and_prepare_file
        with open(output, 'a') as output_file:
            output_file.write('\n')
            ConsoleLogger.create_ics(event, day, output_file)
        # finalise file


class ConsoleLogger(ICSFormatter):

    @staticmethod
    def create_ics(event, day, file_name=None):
        pass
