class Event:

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
        print('DTSTART;TZID=Europe/Warsaw:' + day.strftime('%Y%m%d') + 'T' + self.start_time + '00')
        print('DTEND;TZID=Europe/Warsaw:' + day.strftime('%Y%m%d') + 'T' + self.end_time + '00')
        print('SUMMARY:' + self.class_title)
        print('DESCRIPTION: Prowadzący: ' + self.lecturer)
        print('LOCATION:' + self.location)
        print('TRANSP:OPAQUE')
        print('END:VEVENT')


class FileWriter:

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
        output_file.write('DTSTART;TZID=Europe/Warsaw:' + day.strftime('%Y%m%d') + 'T' + event.start_time + '00\n')
        output_file.write('DTEND;TZID=Europe/Warsaw:' + day.strftime('%Y%m%d') + 'T' + event.end_time + '00\n')
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
