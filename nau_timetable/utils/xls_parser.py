#! /usr/bin/env python

# import sys
# import xlrd
from pprint import pprint

# from ..models import (Faculty, Department, Teacher, Student, Group, Subject,
#                      Building, Room, Lesson, Exam, Event)


def parse_xls(xls_data):
    # import ipdb; ipdb.set_trace()
    pass


def main(src_file):
    f = open()
    f.read()
    f.close
    with open(src_file) as f:
        schedule_data = f.read()

    timetable = parse_xls(schedule_data)
    pprint(timetable)
