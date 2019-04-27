from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Schedule
from schools.models import School
from . import forms


class ScheduleCreate(generic.View):
    model = Schedule
    template_name = "schedules/schedule_add.html"
    form_class = forms.ScheduleForm

    def get(self, request, pk, *args, **kwargs):
        form = forms.ScheduleForm(school_pk=pk)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = forms.ScheduleForm(request.POST, school_pk=pk)
        if form.is_valid():
            schedule_exist = Schedule.objects.filter(
                year=form.cleaned_data['year'],
                class_field=form.cleaned_data['class_field']
            ).count()
            if schedule_exist < 1:
                obj = form.save(commit=False)
                obj.created_by = self.request.user
                obj.school_id = self.kwargs['pk']
                obj.save()
                return redirect('/')
        return self.get(request, pk)


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
