from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms as django_forms
import logging
import django_tables2 as tables

from .forms import LessonForm
from .forms import ScheduleCombo
from .models import Lesson
from .tables import ClassTable
from schools.models import School
from classes_app.models import Class
from schedules.models import Schedule, ScheduleDate
from schedules.forms import ScheduleDateForm


# class SelectYear(generic.ListView):
#     model = School
#     paginate_by = 5
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dates'] = [(for date in School._meta.)]


# class SelectClass(generic.CreateView):
#     template_name = 'lessons_panel/lesson_add.html'
#     lesson_form_class = LessonForm
#
#     def post(self, request, *args, **kwargs):
#         post_data = request.POST or None
#         lesson_form = self.lesson_form_class(post_data, prefix='lesson_form')
#         class_object = Class.objects.get(id=kwargs['pk'])
#         # school_object = School.objects.filter(class__id=kwargs['pk'])
#         # breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')
#         table = ClassTable(Class.objects.filter(school_id=class_object.school_id))
#
#         context = self.get_context_data(lesson_form=lesson_form, table=table)
#
#         if lesson_form.is_valid():
#             self.form_save(lesson_form, class_object.school_id)
#         # if breakes_form.is_valid():
#         #     self.form_save(breakes_form)
#
#         return self.render_to_response(context)
#
#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
#
#     def form_save(self, form, school_id):
#         obj = form.save()
#         obj.created_by = self.request.user
#         obj.school_id = school_id
#         # obj.class_id = self.kwargs['pk']
#         # messages.success(self.request, "{} saved successfully".format(obj.class_id))
#         return obj

def make_schedule_panel(pk):
    days_dict = {1: "Pon", 2: "Wt", 3: "Śr", 4: "Czw", 5: "Pt", 6: "Sob", 7: "Nie"}
    school_object = School.objects.get(id=pk)
    max_lessons = school_object.max_lessons
    work_dict = days_dict.copy()
    for key, value in list(work_dict.items()):
        if str(key) in school_object.weekend_days or value in school_object.weekend_days:
            del work_dict[key]
    return max_lessons, school_object, work_dict


class LessonsPanelView(generic.TemplateView):
    template_name = 'lessons_panel/lesson_add.html'

    # lesson_form_class = LessonForm

    def get(self, request, pk, *args, **kwargs):
        schedules = ScheduleCombo(school_pk=pk)
        max_lessons, school_object, work_dict = make_schedule_panel(pk)
        lesson_form = LessonForm(work_dict=work_dict, max_lessons=max_lessons)

        context = self.get_context_data(
            lesson_form=lesson_form,
            schedule_object=schedules,
            school_object=school_object,
            max_lessons=range(1, max_lessons + 1),
            work_dict=work_dict
        )

        return self.render_to_response(context)

    def post(self, request, pk, *args, **kwargs):
        post_data = request.POST
        lesson_form = LessonForm(post_data)
        schedules = ScheduleCombo(post_data, school_pk=pk)

        if schedules.is_valid():
            class_id = post_data['class_field']
            schedule_id = post_data['schedule']
            errors = lesson_form.errors
            if lesson_form.is_valid():
                self.form_save(lesson_form, class_id, schedule_id)
                messages.success(request, "Dodano lekcje")
                return self.get(request, pk)
        return self.get(request, pk)

    def form_save(self, form, class_id, schedule_id):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.class_field_id = class_id
        obj.schedule_id = schedule_id
        obj.save()
        return obj


def load_schedules(request):
    class_id = request.GET.get('class_field')
    schedules_year = Schedule.objects.filter(class_field_id=int(class_id))
    return render(request, 'lessons_panel/schedules_dropdown_list.html', {'schedules_year': schedules_year})


def load_schedule_panel(request):
    schedule_id = request.GET.get('schedule')
    schedule_object = Schedule.objects.get(id=schedule_id)
    school_id = schedule_object.school_id
    lessons_list = schedule_object.lesson_set.all()
    max_lessons, school_object, work_dict = make_schedule_panel(school_id)
    for lesson in lessons_list:
        lesson.day = int(lesson.day)
    table_string = "<tbody id='table_body'>"

    for key, value in work_dict.items():
        table_string += "<tr><td>" + value + "</td>"
        if lessons_list:
            for i in range(1, max_lessons + 1):
                if_inside = False
                for lesson in lessons_list:
                    if lesson.lesson_number == i and lesson.day == key and not if_inside:
                        table_string += "<td>" + lesson.subject.short_name + "<br>" + \
                                        lesson.room.room_number + "</td>"
                        if_inside = True
                if not if_inside:
                    table_string += "<td></td>"
        table_string += "</tr>"
    table_string += "</tbody>"

    return render(request, 'lessons_panel/schedule_panel.html', {'schedule_selected': schedule_object,
                                                                 'max_lessons': range(1, max_lessons + 1),
                                                                 'schedule_panel': table_string})

    # def post(self, **kwargs):

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     return super(SchoolCreate, self).form_valid(form)
