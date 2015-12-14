# from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render


class ScheduleViewIndex(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class EventScheduleView(View):
    """docstring for ScheduleView"""
    template_name = 'schedule/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


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
