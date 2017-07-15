from abc import abstractmethod, ABCMeta
import sys


class ICSFormatter(ABCMeta):

    @staticmethod
    @abstractmethod
    def create_ics(event, day, output):
        raise NotImplementedError('Can\'t call abstract method!')


class FileCreator(ICSFormatter):

    @staticmethod
    def create_ics(event, day, output):

        with open(output, 'a') as output_file:
            output_file.write('\n')
            ConsoleLogger.create_ics(event, day, output_file)


class ConsoleLogger(ICSFormatter):

    @staticmethod
    def create_ics(event, day, output):

        buffer = '\n'.join([
            'BEGIN:VEVENT',
            'DTSTART;TZID={}:{}T{}00'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.start_time),
            'DTEND;TZID={}:{}T{}00'.format(event.TIME_ZONE, day.strftime('%Y%m%d'), event.end_time),
            'SUMMARY:{}'.format(event.class_title),
            'DESCRIPTION: Prowadzący: {}; Rodzaj zajęć: {}'.format(event.teacher, event.class_type),
            'LOCATION:{}'.format(event.location),
            'TRANSP:OPAQUE',
            'END:VEVENT',
        ])

        output.write(buffer)
