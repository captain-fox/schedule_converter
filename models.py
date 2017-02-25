import csv


class Event:

    TIME_ZONE = 'Europe/Warsaw'

    def __init__(self):

        self.class_title = ''
        self.week_day = ''
        self.start_time = ''
        self.end_time = ''
        self.weeks = ''
        self.class_type = ''
        self.location = ''
        self.lecturer = ''

    def simulate_ics_output(self, day):

        print('BEGIN:VEVENT')
        print('DTSTART;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00')
        print('DTEND;TZID=' + self.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00')
        print('SUMMARY:' + self.class_title)
        print('DESCRIPTION: Prowadzący: ' + self.lecturer)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')


class FileWriter:

    @staticmethod
    def read_csv_file(filename):

        csv_rows = []
        with open(filename, 'rt', encoding='windows 1250') as csv_input:
            reader = csv.reader(csv_input, delimiter=';')
            for row in reader:
                csv_rows.append(row)
        return csv_rows

    @staticmethod
    def create_and_prepare_file(grouptitle):

        filename = (grouptitle + '.ics')
        newfile = open(filename, 'w')
        newfile.write('BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n\n')
        newfile.close()
        return filename

    @staticmethod
    def append_to_ics(event, output_file, day):

        open(output_file, 'a')
        output_file.write('BEGIN:VEVENT\n')
        output_file.write('DTSTART;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.start_time + '00\n')
        output_file.write('DTEND;TZID=' + event.TIME_ZONE + ':' + day.strftime('%Y%m%d') + 'T' + event.end_time + '00\n')
        output_file.write('SUMMARY:' + event.class_title + '\n')
        output_file.write('DESCRIPTION: Prowadzący: ' + event.lecturer + '\n')
        output_file.write('LOCATION:' + event.location + '\n')
        output_file.write('TRANSP:OPAQUE\n')
        output_file.write('END:VEVENT\n\n')
        output_file.close()

    @staticmethod
    def finalise_file(output_file):

        open(output_file, 'a')
        output_file.write('END:VCALENDAR')
        output_file.close()


class Group:

    __HEADERS__ = {
        'Ref': '',
        'Day': '',
        'Time': '',
        'Weeks': '',
        'EventCat': '',
        'Module': '',
        'Room': '',
        'Surname': '',
        'Group': '',
    }

    @staticmethod
    def get_groups(rows):

        number_of_rows = sum(1 for row in rows[1:])
        # to store unique values only
        groups = set([])
        counter = 1
        try:
            while counter < number_of_rows:
                groups.add(rows[counter][12])
                counter += 1
        except IndexError:
            print('Oops. Trying to read white spaces after table. IndexError at row:', counter)
        # Kicking empty space ''
        if '' in groups:
            groups.remove('')
        return sorted(groups)
