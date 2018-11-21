from django.shortcuts import render
from django.views import generic
# noinspection PyUnresolvedReferences
from start_page import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class SubjectView(generic.ListView):
    model = models.Schedule
    template_name = 'object_creation/subjects.html'
    context_object_name = 'all_subjects'

    def get_queryset(self):
        user = self.request.user
        schedule = models.Schedule.objects.filter(user_id=user.id)
        subjects = models.Subject.objects.get(schedule_id=schedule.id)
        return subjects


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

