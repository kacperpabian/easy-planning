from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Schedule
from .models import ScheduleDate
from schools.models import School
from . import forms


class ScheduleCreate(generic.TemplateView):
    template_name = "schedules/schedule_add.html"

    def get(self, request, pk, *args, **kwargs):
        schedule_form = forms.ScheduleForm(school_pk=pk)
        schedule_date_form = forms.ScheduleDateForm

        context = self.get_context_data(
            schedule_form=schedule_form,
            schedule_date_form=schedule_date_form
        )
        return self.render_to_response(context)

    def post(self, request, pk, *args, **kwargs):
        post_data = request.POST

        schedule_form = forms.ScheduleForm(post_data, school_pk=pk)
        schedule_date_form = forms.ScheduleDateForm(post_data)

        # errors = schedules.errors

        if schedule_date_form.is_valid() and schedule_form.is_valid():
            year = schedule_date_form.cleaned_data["year"]
            if ScheduleDate.objects.filter(year=year).count() < 1:
                self.form_save_date(schedule_date_form)
            self.form_save_schedule(
                schedule_form,
                ScheduleDate.objects.get(year=str(year)).id,
                pk
                )
        return self.get(request, pk)

    def form_save_date(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()
        return obj

    def form_save_schedule(self, form, schedule_date_id, school_id):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.year_id = schedule_date_id
        obj.school_id = school_id
        obj.save()
        return obj


class ScheduleDelete(generic.DeleteView):
    model = Schedule
    template_name = "schedules/schedule_delete.html"
    # context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(ScheduleDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['schedule'] = get_object_or_404(Schedule, id=self.kwargs.get('pk', ))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:schools', kwargs={'pk': school_id})
# Create your views here.
