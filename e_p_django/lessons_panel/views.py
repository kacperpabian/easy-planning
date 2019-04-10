from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms as django_forms

import django_tables2 as tables

from .forms import LessonForm
from .forms import ScheduleCombo
from .models import Lesson
from .tables import ClassTable
from schools.models import School
from classes_app.models import Class
from schedules.models import Schedule


# class SelectYear(generic.ListView):
#     model = School
#     paginate_by = 5
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dates'] = [(for date in School._meta.)]


class SelectClass(generic.CreateView):
    template_name = 'lessons_panel/lesson_add.html'
    lesson_form_class = LessonForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST or None
        lesson_form = self.lesson_form_class(post_data, prefix='lesson_form')
        class_object = Class.objects.get(id=kwargs['pk'])
        # school_object = School.objects.filter(class__id=kwargs['pk'])
        # breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')
        table = ClassTable(Class.objects.filter(school_id=class_object.school_id))

        context = self.get_context_data(lesson_form=lesson_form, table=table)

        if lesson_form.is_valid():
            self.form_save(lesson_form, class_object.school_id)
        # if breakes_form.is_valid():
        #     self.form_save(breakes_form)

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def form_save(self, form, school_id):
        obj = form.save()
        obj.created_by = self.request.user
        obj.school_id = school_id
        # obj.class_id = self.kwargs['pk']
        # messages.success(self.request, "{} saved successfully".format(obj.class_id))
        return obj


class LessonsPanelView(generic.TemplateView):
    template_name = 'lessons_panel/lesson_add.html'
    lesson_form_class = LessonForm
    combo_schedule_form = ScheduleCombo

    def get(self, request, *args, **kwargs):
        lesson_form = self.lesson_form_class
        combo_schedule_form = self.combo_schedule_form
        # breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')
        table = ClassTable(Class.objects.filter(school_id=kwargs['pk']))
        school_object = School.objects.get(id=kwargs['pk'])
        # schedule_object = Schedule.objects.get(school_id=kwargs['pk'])

        context = self.get_context_data(
            lesson_form=lesson_form,
            table=table,
            school_object=school_object,
            schedule_object=combo_schedule_form
        )

        return self.render_to_response(context)
    #
    # def post(self, **kwargs):


    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     return super(SchoolCreate, self).form_valid(form)
