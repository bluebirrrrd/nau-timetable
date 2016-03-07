from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import (Faculty, Department, Teacher, Student, Group, Subject,
                      Building, Room, Lesson, Exam, Event)


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ('url', 'name', 'full_name', 'head')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'name', 'full_name', 'faculty')


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'last_name', 'middle_name', 'first_name', 'name',
                  'full_name', 'position', 'position_text')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'last_name', 'middle_name', 'first_name', 'group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'degree', 'type', 'commander')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('url', 'short_name', 'full_name')


class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ('url', 'name', 'latitude', 'longitude')


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'name', 'full_name', 'building', 'capacity', 'type',
                  'type_text', 'department')


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ('url', 'number', 'number_text', 'day', 'day_text', 'week',
                  'week_text', 'type', 'type_text', 'subject', 'subject_name',
                  'teacher', 'teacher_short_name', 'groups', 'groups_names',
                  'subgroup_num', 'subgroup_name', 'room', 'room_full_name')


class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('url', 'subject', 'subject_name', 'teacher',
                  'teacher_short_name', 'groups', 'groups_names', 'date',
                  'type', 'type_text', 'room', 'room_full_name')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'description', 'date', 'type',
                  'type_text', 'room', 'room_full_name')
