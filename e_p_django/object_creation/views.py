from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django_tables2 import RequestConfig, SingleTableView
# noinspection PyUnresolvedReferences
from start_page import models
from . import forms, tables
from django.urls import reverse_lazy


class ScheduleChange(generic.UpdateView):
    form_class = forms.ScheduleForm
    template_name = 'object_creation/change_schedule.html'
    template_name_suffix = '_update_form'

    def get_queryset(self):
        user = self.request.user
        return models.Schedule.objects.filter(user_id=user.id)

    # display blank form
    def get(self, request, **kwargs):
        schedule = self.get_object()
        data = {'name': schedule.name,
                'cycle': schedule.cycle,
                'school_year': schedule.school_year,
                'school_name': schedule.school_name,
                'description': schedule.description,
                'weekend_days': schedule.weekend_days,
                'start_time': schedule.start_time,
                'max_lessons': schedule.max_lessons}
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if form.changed_data:
                schedule = form.save(commit=False)
                schedule.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")

        return render(request, self.template_name, {'form': form})


class ScheduleDelete(generic.DeleteView):
    model = models.Schedule
    template_name = "object_delete/schedule_delete.html"
    success_url = reverse_lazy('start_page:schedules')


class SubjectsView(SingleTableView):
    model = models.Subject
    template_name = 'object_creation/subjects.html'
    table_class = tables.SubjectTable

    def get_context_data(self, **kwargs):
        context = super(SubjectsView, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        schedule = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return models.Subject.objects.filter(schedule_id=schedule.id)


class SubjectCreate(generic.CreateView):
    model = models.Subject
    template_name = "object_creation/subject_add.html"
    form_class = forms.SubjectForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.schedule_id = self.kwargs['pk']
        return super(SubjectCreate, self).form_valid(form)


class SubjectDelete(generic.DeleteView):
    model = models.Subject
    template_name = "object_delete/subject_delete.html"
    context_object_name = 'subject'

    def get_success_url(self):
        schedule_id = self.object.schedule_id
        return reverse_lazy('start_page:object_creation:subjects', kwargs={'pk': schedule_id})


class SubjectUpdate(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    template_name_suffix = '_update_form'
