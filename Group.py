from InputConverter import *
from FileHandler import *


class Group:

    @staticmethod
    def get_groups(rows):
        row_counter = 1

        try:
            # using set to store unique values only
            groups = set([])

            for row in rows[1:len(rows) - 1]:
                if row[InputConverter.group_column()] == '':
                    continue
                groups.add(row[InputConverter.group_column()])
                row_counter += 1

            # Kicking out empty space element from groups
            # if '' in groups:
            #     groups.remove('')

            print('{} unique groups found'.format(len(groups)))
            return sorted(groups)

        except IndexError:
            print('Oops. Trying to read white spaces after table. IndexError in row: {}'.format(row_counter))
            sys.exit(0)
        except TypeError:
            print('get_groups method in \'Groups\' tried to read non-existing file or file with unexpected structure.')
            sys.exit(0)
        except Exception as e:
            print('Unexpected type of exception: "{}" occurred in get_groups method.'.format(e))
            sys.exit(0)