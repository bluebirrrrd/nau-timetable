from django.conf.urls import url

from . import views


entity_uri = r'^(?P<type>group|teacher|department|building)/(?P<slug>[\-\w]+)/'

urlpatterns = [
    url(r'^$', views.ScheduleViewIndex.as_view()),
    url(r'^event/?$', views.EventScheduleView.as_view(),
        name='events'),
    url(r'^event/(?P<slug>[\-\w]+)/?$', views.EventDetailView.as_view(),
        name='event'),
    url(r'^group/(?P<slug>[\-\w]+)/?$', views.GroupScheduleView.as_view()),
    url(r'^teacher/(?P<slug>[\-\w]+)/?$', views.TeacherScheduleView.as_view()),
    url(r'^department/(?P<slug>[\-\w]+)/?$', views.ScheduleView.as_view()),
    url(r'^building/(?P<slug>[\-\w]+)/?$',
        views.BuildingScheduleView.as_view()),
    url(r'^group/(?P<slug>[\-\w]+)/exams/?$',
        views.ExamScheduleView.as_view()),
    url(entity_uri + r'building/free-rooms/?$',
        views.FreeRoomScheduleView.as_view()),
    url(r'^teacher/(?P<slug>[\-\w]+)/consultations/?$',
        views.ConsultationScheduleView.as_view()),
]
