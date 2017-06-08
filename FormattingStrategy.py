from abc import abstractmethod, ABCMeta


class ICSFormatter(ABCMeta):

    @classmethod
    def select_processing_method(mcs, filename):

        if filename is None:
            return ConsoleLogger.pass_data
        else:
            return FileCreator.pass_data

    @staticmethod
    @abstractmethod
    def pass_data(event, day, filename=None): pass


class FileCreator(ICSFormatter):

    @staticmethod
    def pass_data(event, day, file_name=None):
        output_file = open(file_name, 'a')
        output_file.write('BEGIN:VEVENT\n')
        output_file.write('DTSTART;TZID={}:{}T{}00\n'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.start_time))
        output_file.write('DTEND;TZID={}:{}T{}00\n'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.end_time))
        output_file.write('SUMMARY:{}\n'.format(event.class_title))
        output_file.write('DESCRIPTION: Prowadzący: {}; Rodzaj zajęć: {}\n'.format(event.teacher, event.class_type))
        output_file.write('LOCATION:{}\n'.format(event.location))
        output_file.write('TRANSP:OPAQUE\n')
        output_file.write('END:VEVENT\n\n')
        output_file.close()


class ConsoleLogger(ICSFormatter):

    @staticmethod
    def pass_data(event, day, file_name=None):
        print('BEGIN:VEVENT')
        print('DTSTART;TZID={}:{}T{}00'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.start_time))
        print('DTEND;TZID={}:{}T{}00'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.end_time))
        print('SUMMARY:{}'.format(event.class_title))
        print('DESCRIPTION: Prowadzący: {}; Rodzaj zajęć: {}'.format(event.teacher, event.class_type))
        print('LOCATION:{}'.format(event.location))
        print('TRANSP:OPAQUE')
        print('END:VEVENT')
