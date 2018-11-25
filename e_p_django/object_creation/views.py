from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
# noinspection PyUnresolvedReferences
from start_page import models
from . import forms
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
# class DetailView(generic.DetailView):
#     model = models.Schedule
#     template_name = "start_page/schedule_detail.html"
#
#
# class SubjectCreate(CreateView):
#     model = models.Schedule
#     fields = ['name', 'cycle', 'school_year', 'school_name', 'description', 'weekend_days', 'start_time',
#               'max_lessons']
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.created_by = self.request.user
#         obj.user_id = self.request.user.id
#         return super(ScheduleCreate, self).form_valid(form)

