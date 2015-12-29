# from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import render

from ..models import Event, Lesson, Group


class ScheduleViewIndex(TemplateView):
    """docstring for ScheduleView"""
    model = Lesson
    context_object_name = "lessons"
    template_name = 'schedule/index.html'


class EventScheduleView(ListView):
    """docstring for ScheduleView"""
    model = Event
    context_object_name = 'event_list'
    template_name = 'schedule/events.html'


class EventDetailView(DetailView):
    """docstring for ScheduleView"""
    model = Event
    context_object_name = 'event'
    template_name = 'schedule/event.html'


class GroupScheduleView(DetailView):
    """docstring for ScheduleView"""
    model = Group
    context_object_name = "group"
    template_name = 'schedule/group_schedule.html'

    slug_field = 'name'

    def get_context(self):
        context = super(GroupScheduleView, self).get_context()
        context['lessons'] = self.model.lessons.all()
        return context


class ScheduleView(ListView):
    """docstring for ScheduleView"""
    model = Lesson
    context_object_name = "lessons"
    template_name = 'schedule/index.html'

    def get_queryset(self):
        stype = self.kwargs['type']
        if stype == 'group':
            stype += 's'
        qsargs = {
            stype + '__name': self.kwargs['slug']
        }
        qs = self.model.objects.filter(**qsargs)
        return qs


class ExamScheduleView(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class FreeRoomScheduleView(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ConsultationScheduleView(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
