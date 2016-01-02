# from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView, TemplateView
from django.shortcuts import render

from ..models import Event, Lesson, Group, Teacher, Building


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

    def get_context_data(self, *args, **kwargs):
        context = super(GroupScheduleView, self).get_context_data(*args,
                                                                  **kwargs)
        context['timetable'] = (
            {
                'week': (week_num, Lesson.get_week_text(week_num)),
                'days': [
                    {
                        'day': day,
                        'lessons': kwargs['object'].lesson_set.filter(
                            week=week_num, day=day[0]).order_by('number')}
                        for day in Lesson.DAY_LIST
                ]
            } for week_num in (True, False)
        )

        return context


class TeacherScheduleView(DetailView):
    """docstring for ScheduleView"""
    model = Teacher
    context_object_name = "teacher"
    template_name = 'schedule/teacher_schedule.html'

    slug_field = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super(TeacherScheduleView, self).get_context_data(*args,
                                                                    **kwargs)
        context['timetable'] = (
            {
                'week': (week_num, Lesson.get_week_text(week_num)),
                'days': [
                    {
                        'day': day,
                        'lessons': kwargs['object'].lesson_set.filter(
                            week=week_num, day=day[0]).order_by('number')}
                        for day in Lesson.DAY_LIST
                ]
            } for week_num in (True, False)
        )

        return context


class BuildingScheduleView(DetailView):
    """docstring for ScheduleView"""
    model = Building
    context_object_name = "building"
    template_name = 'schedule/building_schedule.html'

    slug_field = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super(BuildingScheduleView, self).get_context_data(*args,
                                                                     **kwargs)
        context['timetable'] = (
            {
                'room': room,
                'schedule': (
                    {
                        'week': (week_num, Lesson.get_week_text(week_num)),
                        'days': [
                            {
                                'day': day,
                                'lessons': room.lesson_set.filter(
                                    week=week_num,
                                    day=day[0]).order_by('number')}
                                for day in Lesson.DAY_LIST
                        ]
                    } for week_num in (True, False)
                )
            } for room in kwargs['object'].room_set.all()
        )

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
