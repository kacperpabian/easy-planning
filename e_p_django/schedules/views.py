from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Schedule
from schools.models import School
from . import forms


class ScheduleCreate(generic.CreateView):
    model = Schedule
    template_name = "schedules/schedule_add.html"
    form_class = forms.ScheduleForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(ScheduleCreate, self).form_valid(form)


class ScheduleDelete(generic.DeleteView):
    model = Schedule
    template_name = "schedules/schedule_delete.html"

    # context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(ScheduleDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['schedule'] = get_object_or_404(Schedule, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:schools', kwargs={'pk': school_id})
# Create your views here.
