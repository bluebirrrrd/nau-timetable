from django.conf.urls import url

from . import views


entity_uri = r'^(?P<type>group|teacher|department|building)/(?P<slug>[\-\w]+)/'

urlpatterns = [
    url(r'^$', views.ScheduleViewIndex.as_view()),
    url(r'^event/?$', views.EventScheduleView.as_view(),
        name='events'),
    url(r'^event/(?P<slug>[\-\w]+)/?$', views.EventDetailView.as_view(),
        name='event'),
    url(entity_uri + r'?$', views.ScheduleView.as_view()),
    url(entity_uri + r'exams/?$', views.ExamScheduleView.as_view()),
    url(entity_uri + r'free-rooms/?$', views.FreeRoomScheduleView.as_view()),
    url(entity_uri + r'consultations/?$',
        views.ConsultationScheduleView.as_view()),
]
