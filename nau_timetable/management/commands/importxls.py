from xlrd import open_workbook

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """docstring for Command"""

    help = 'Imports given xls file with schedule to db'

    def add_arguments(self, parser):
        parser.add_argument('xls_filename', type=str)

    def handle(self, *args, **options):
        if not options.get('xls_filename'):
            raise CommandError('Pass the correct xls file, Luke!')

        # detecting whether the row is empty, title, subtitle, schedule of
        # the whole group or a subgroup
        def get_row_category(rownum):
            row = sheet.row_values(rownum)
            if rownum + 1 < sheet.nrows:
                row2 = sheet.row_values(rownum + 1)
            if row[0].strip() == 'НАУ':
                return 'title'
            if row[0].strip() == 'Пара' or row[2].strip() == 'Підгрупа 1':
                return 'subtitle'
            if row[8].strip() == '' and row[6].strip() == '':
                return 'empty string'

            try:
                if row2[3].strip() != '' or row2[7].strip() != '':
                    return 'subgroup'
                if row2[8].strip() != '':
                    return 'group_lesson'
            except:
                return 'unknown'

            return 'unknown'

        wb = open_workbook(options['xls_filename'], on_demand=True)
        sheet = wb.get_sheet(0)

        # list of parsed items
        lessons = []

        # basic structure of lesson
        base_lesson = {}

        rownum = 0
        while rownum < sheet.nrows:
            category = get_row_category(rownum)
            row = sheet.row_values(rownum)
            # print(sheet.row_values(rownum))
            # print(category)

            if category == 'subtitle':
                rownum += 4
                # there are always 3 empty strings after the subtitle
                continue

            if category == 'empty string':
                rownum += 1
                continue

            if category == 'title':
                # reset base_lesson if we've found the next week
                base_lesson = {}
                base_lesson['faculty'], \
                    base_lesson['group'] = row[1].split(' ')
                base_lesson['major'] = row[4]
                base_lesson['week'] = row[11].endswith('1')

                rownum += 3
                continue

            if rownum + 1 < sheet.nrows:
                row2 = sheet.row_values(rownum + 1)

            if category == 'group_lesson':
                lesson_num = int(row[1])
                if lesson_num == 1:
                    # row with 1st lesson contains data about weekday
                    base_lesson['day'] = row[0]

                lesson = base_lesson.copy()
                lesson['num'] = lesson_num
                lesson['subject'] = row[2].strip()
                lesson['room'] = row[6].replace(' ', '')
                lesson['type'] = row[8].strip()
                lesson['teacher'] = {
                    'name': row[10].strip(),
                    'position': row2[8].strip(),
                }
                lessons.append(lesson)

                rownum += 2
                continue

            elif category == 'subgroup':
                if len(row[2]) > 0:  # schedule of subgroup 1
                    lesson_num = int(row[1])
                    if lesson_num == 1:
                        base_lesson['day'] = row[0]

                    lesson = base_lesson.copy()
                    lesson['num'] = lesson_num
                    lesson['subject'] = row[2].strip()
                    lesson['room'] = row2[2].replace(' ', '')
                    lesson['type'] = row2[3].strip()
                    lesson['teacher'] = {
                        'name': row[5].strip(),
                        'position': row2[4].strip(),
                    }
                    lessons.append(lesson)

                if len(row[6]) > 0:
                    lesson_num = int(row[1])
                    if lesson_num == 1:
                        base_lesson['day'] = row[0]

                    lesson = base_lesson.copy()
                    lesson['num'] = lesson_num
                    lesson['subject'] = row[6].strip()
                    lesson['room'] = row2[6].replace(' ', '')
                    lesson['type'] = row2[7].strip()
                    lesson['teacher'] = {
                        'name': row[11].strip(),
                        'position': row2[9].strip(),
                    }
                    lessons.append(lesson)

                rownum += 2
                continue

            rownum += 1

        from pprint import pprint
        pprint(lessons)
