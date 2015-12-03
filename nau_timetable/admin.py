from django.contrib import admin
from .models import (Faculty, Department, Teacher, Student, Group, Subject,
                     Building, Room, Lesson, Exam, Event)

for cls in (Faculty, Department, Teacher, Student, Group, Subject, Building,
            Room, Lesson, Exam, Event):
    admin.site.register(cls)
