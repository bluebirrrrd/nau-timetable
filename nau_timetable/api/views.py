from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import (Faculty, Department, Teacher, Student, Group, Subject,
                      Building, Room, Lesson, Exam, Event)

from .serializers import (UserSerializer, FacultySerializer,
                          DepartmentSerializer, TeacherSerializer,
                          StudentSerializer, GroupSerializer,
                          SubjectSerializer, BuildingSerializer,
                          RoomSerializer, LessonSerializer, ExamSerializer,
                          EventSerializer, ScheduleSerializer)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = ScheduleSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def schedule(request, type_, name):
    mdl = None

    if type_ == 'group':
        mdl = Group
    elif type_ == 'teacher':
        mdl = Teacher
    elif type_ == 'room':
        mdl = Room

    queryset = mdl.objects.filter(name=name)
    serializer = ScheduleSerializer(queryset, context={'request': request})
    return Response(serializer.data)
