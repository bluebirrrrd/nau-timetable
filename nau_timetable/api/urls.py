from django.conf.urls import include, url
from rest_framework import routers

from .views import (UserViewSet, FacultyViewSet, DepartmentViewSet,
                    TeacherViewSet, StudentViewSet, GroupViewSet,
                    SubjectViewSet, BuildingViewSet, RoomViewSet,
                    LessonViewSet, ExamViewSet, EventViewSet)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
]
