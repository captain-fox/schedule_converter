from abc import abstractmethod, ABCMeta

class ICSFormatter(ABCMeta):

    @classmethod
    def select_processing_method(mcs, filename):

        if filename is None:
            return ConsoleLogger
        else:
            return FileCreator

    @staticmethod
    @abstractmethod
    def pass_data(event, day, filename=None): pass


class FileCreator(ICSFormatter):

    @staticmethod
    def pass_data(event, day, file_name=None):
        output_file = open(file_name, 'a')
        output_file.write('BEGIN:VEVENT\n')
        output_file.write('DTSTART;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.start_time + '00\n')
        output_file.write('DTEND;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.end_time + '00\n')
        output_file.write('SUMMARY:' + event.class_title + '\n')
        output_file.write('DESCRIPTION: Prowadzący: ' + event.teacher + '\n')
        output_file.write('LOCATION:' + event.location + '\n')
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
