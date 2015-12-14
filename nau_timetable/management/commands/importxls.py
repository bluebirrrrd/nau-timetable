from decimal import Decimal
from xlrd import open_workbook

from django.core.management.base import BaseCommand, CommandError

from nau_timetable.models import (Subject, Lesson,
                                  Group, Teacher,
                                  Room, Building)


class Command(BaseCommand):
    """docstring for Command"""

    help = 'Imports given xls file with schedule to db'

    def add_arguments(self, parser):
        parser.add_argument('xls_filename', type=str)

    def handle(self, *args, **options):
        if not options.get('xls_filename'):
            raise CommandError('Pass the correct xls file, Luke!')

        _DAY_LIST = {'пнд': 1, 'втр': 2, 'срд': 3, 'чтв': 4, 'птн': 5,
                     'сбт': 6}

        _TYPE_LIST = {'лекція': 0, 'практичне': 1, 'лабораторна': 2}
        _POSITIONS_LIST = {'аспірант': 0, 'асистент': 1, 'старший викл': 2,
                           'доцент': 3, 'професор': 4}

        _NAU_COORDS = {'lat': Decimal('50.4374764'),
                       'lon': Decimal('30.4261333')}

        def save_subj(lesson):
            assert isinstance(lesson, dict), 'lesson should be dict instance'
            # First, create Teacher record
            tchr = lesson['teacher']
            tchr['name'] = tchr['name'].strip().split(' ')
            tchr['name'].append(tchr['name'][1].split('.')[0])
            tchr['name'][1] = tchr['name'][1].split('.')[1].strip('.')

            teacher, teacher_created = Teacher.objects.get_or_create(
                last_name=lesson['teacher']['name'][0],
                position=lesson['teacher']['position'],
                defaults={
                    # 'last_name': tchr['name'][0],
                    'first_name': tchr['name'][1],
                    'middle_name': tchr['name'][2],
                    # 'position': tchr['position'],
                })
            teacher.save()

            sbj, created_sbj = \
                Subject.objects.get_or_create(full_name=lesson['subject'])
            sbj.save()

            building, created_building = \
                Building.objects.get_or_create(
                    name=lesson['room'].split('.')[0],
                    defaults={'latitude': _NAU_COORDS['lat'],
                              'longitude': _NAU_COORDS['lon']})
            building.save()
            room, created_room = \
                Room.objects.get_or_create(name=lesson['room'],
                                           defaults={'type': lesson['type'],
                                                     'building': building})
            room.save()

            group = Group.objects.filter(name__endswith=lesson['group'])
            if not group:
                group = Group(name=lesson['group'],
                              type=0,
                              degree=0)  # TODO: autonegotiate this
                group.save()

            l = Lesson(
                number=lesson['num'],
                day=lesson['day'],  # get day num
                week=lesson['week'],
                type=lesson['type'],  # get type id
                subject=sbj,  # Foreign+
                teacher=teacher,  # Foreign+
                # groups=lesson['num'],   # Foreign, Many+
                subgroup_num=lesson.get('subgroup'),  # fetch num of group
                room=room,  # Foreign+
            )

            # l.save()
            # l.groups.add(group)
            l.save()

        # detecting whether the row is empty, title, subtitle, schedule of
        # the whole group or a subgroup
        def get_row_category(rownum):
            row = sheet.row_values(rownum)
            if rownum + 1 < sheet.nrows:
                row2 = sheet.row_values(rownum + 1)
            if row[0].strip().lower() == 'нау':
                return 'title'
            if row[0].strip().lower() == 'пара' or \
               row[2].strip().lower() == 'підгрупа 1':
                return 'subtitle'
            if len(row[8].strip()) + len(row[6].strip()) < 1:
                return 'empty string'

            try:
                if len(row2[3].strip()) + len(row2[7].strip()) > 0:
                    return 'subgroup'
                if len(row2[8].strip()) > 0:
                    return 'group_lesson'
            except:
                return 'unknown'

            return 'unknown'

        def parse_title(row):
            base_lesson = {}
            base_lesson['faculty'], \
                base_lesson['group'] = row[1].strip().split(' ')
            base_lesson['major'] = row[4].strip()
            base_lesson['week'] = row[11].strip().endswith('1')
            base_lesson['subgroup'] = None
            return base_lesson

        def parse_group_lesson(row, row2, base_lesson):
            lesson_num = int(row[1])
            if lesson_num == 1:
                # row with the 1st lesson contains data about weekday
                base_lesson['day'] = _DAY_LIST[row[0].strip().lower()]

            lesson = base_lesson.copy()
            lesson['num'] = lesson_num
            lesson['subject'] = row[2].strip()
            lesson['room'] = row[6].replace(' ', '')
            lesson['type'] = _TYPE_LIST[row[8].strip()
                                        # Someone 'wise' put latin i instead
                                        # of cyrillic one, fixing this:
                                        .lower().replace('i', 'і')]
            lesson['teacher'] = {
                'name': row[10].strip(),
                'position': _POSITIONS_LIST[row2[8].strip().lower()],
            }
            return lesson

        def parse_subgroup1_lesson(row, row2, base_lesson):
            lesson_num = int(row[1])
            if lesson_num == 1:
                base_lesson['day'] = _DAY_LIST[row[0].strip().lower()]

            lesson = base_lesson.copy()
            lesson['num'] = lesson_num
            lesson['subject'] = row[2].strip()
            lesson['room'] = row2[2].replace(' ', '')
            lesson['type'] = _TYPE_LIST[row2[3].strip().lower()]
            lesson['teacher'] = {
                'name': row2[5].strip(),
                'position': _POSITIONS_LIST[row2[4].strip().lower()],
            }
            lesson['subgroup'] = 1
            return lesson

        def parse_subgroup2_lesson(row, row2, base_lesson):
            lesson_num = int(row[1])
            if lesson_num == 1:
                base_lesson['day'] = _DAY_LIST[row[0].strip().lower()]

            lesson = base_lesson.copy()
            lesson['num'] = lesson_num
            lesson['subject'] = row[6].strip()
            lesson['room'] = row2[6].replace(' ', '')
            lesson['type'] = _TYPE_LIST[row2[7].strip().lower()]
            lesson['teacher'] = {
                'name': row2[11].strip(),
                'position': _POSITIONS_LIST[row2[9].strip().lower()],
            }
            lesson['subgroup'] = 2
            return lesson

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
                base_lesson = parse_title(row)

                rownum += 3
                continue

            if rownum + 1 < sheet.nrows:
                row2 = sheet.row_values(rownum + 1)

            if category == 'group_lesson':
                lesson = parse_group_lesson(row, row2, base_lesson)
                lessons.append(lesson)

                rownum += 2
                continue

            elif category == 'subgroup':
                if len(row[2].strip()) > 0:  # schedule of subgroup 1
                    lesson = parse_subgroup1_lesson(row, row2, base_lesson)
                    lessons.append(lesson)

                if len(row[6].strip()) > 0:  # schedule of subgroup 2
                    lesson = parse_subgroup2_lesson(row, row2, base_lesson)
                    lessons.append(lesson)

                rownum += 2
                continue

            rownum += 1

        from pprint import pprint
        pprint(lessons)

        for l in lessons:
            save_subj(l)
