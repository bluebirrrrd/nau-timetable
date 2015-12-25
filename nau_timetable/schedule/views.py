# from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render

from ..models import Event


class ScheduleViewIndex(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


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


class ScheduleView(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


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
