from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

import django_tables2 as tables

from .forms import LessonForm
from .models import Lesson
from .tables import ClassTable
from schools.models import School
from classes_app.models import Class


# class SelectClass(generic.TemplateView):
#
#     def get_context_data(self):


class LessonsPanelView(generic.TemplateView):
    template_name = 'lessons_panel/lesson_add.html'
    lesson_form_class = LessonForm
    # breakes_form_class = forms.SchoolBreakesForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST or None
        lesson_form = self.lesson_form_class(post_data, prefix='lesson_form')
        # breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')
        table = ClassTable(Class.objects.filter(school_id=kwargs['pk']))

        context = self.get_context_data(lesson_form=lesson_form, table=table)

        if lesson_form.is_valid():
            self.form_save(lesson_form)
        # if breakes_form.is_valid():
        #     self.form_save(breakes_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        # messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     return super(SchoolCreate, self).form_valid(form)
