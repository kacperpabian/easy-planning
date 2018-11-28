from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django_tables2 import (
    SingleTableView,
    LazyPaginator
)
# noinspection PyUnresolvedReferences
from start_page import models
from . import forms, tables
from django.urls import reverse_lazy


class ScheduleChange(generic.UpdateView):
    form_class = forms.ScheduleForm
    template_name = 'object_edit/schedule_edit.html'
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
    paginator_class = LazyPaginator

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
    # context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        schedule_id = self.object.schedule_id
        context = super(SubjectDelete, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=schedule_id)
        context['subject'] = get_object_or_404(models.Subject, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        schedule_id = self.object.schedule_id
        return reverse_lazy('start_page:object_creation:subjects', kwargs={'pk': schedule_id})


class SubjectUpdate(generic.UpdateView):
    model = models.Subject
    form_class = forms.SubjectForm
    template_name = "object_edit/subject_edit.html"
    template_name_suffix = '_update_form'

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


class RoomCreate(generic.CreateView):
    model = models.Room
    template_name = "object_creation/room_add.html"
    form_class = forms.RoomForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.schedule_id = self.kwargs['pk']
        return super(RoomCreate, self).form_valid(form)


class RoomsView(SingleTableView):
    model = models.Room
    template_name = 'object_creation/rooms.html'
    table_class = tables.RoomsTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(RoomsView, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        schedule = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return models.Room.objects.filter(schedule_id=schedule.id)


class RoomDelete(generic.DeleteView):
    model = models.Room
    template_name = "object_delete/room_delete.html"

    def get_context_data(self, **kwargs):
        schedule_id = self.object.schedule_id
        context = super(RoomDelete, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=schedule_id)
        context['room'] = get_object_or_404(models.Room, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        schedule_id = self.object.schedule_id
        return reverse_lazy('start_page:object_creation:rooms', kwargs={'pk': schedule_id})


class RoomUpdate(generic.UpdateView):
    model = models.Room
    form_class = forms.RoomForm
    template_name = "object_edit/room_edit.html"
    template_name_suffix = '_update_form'

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


class TeacherCreate(generic.CreateView):
    model = models.Teacher
    template_name = "object_creation/teacher_add.html"
    form_class = forms.TeacherForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.schedule_id = self.kwargs['pk']
        return super(TeacherCreate, self).form_valid(form)


class TeacherView(SingleTableView):
    model = models.Teacher
    template_name = 'object_creation/teachers.html'
    table_class = tables.TeacherTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        schedule = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return models.Teacher.objects.filter(schedule_id=schedule.id)


class TeacherDelete(generic.DeleteView):
    model = models.Teacher
    template_name = "object_delete/teacher_delete.html"

    def get_context_data(self, **kwargs):
        schedule_id = self.object.schedule_id
        context = super(TeacherDelete, self).get_context_data(**kwargs)
        context['schedule'] = get_object_or_404(models.Schedule, id=schedule_id)
        context['teacher'] = get_object_or_404(models.Teacher, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        schedule_id = self.object.schedule_id
        return reverse_lazy('start_page:object_creation:rooms', kwargs={'pk': schedule_id})


class TeacherUpdate(generic.UpdateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "object_edit/teacher_edit.html"
    template_name_suffix = '_update_form'

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


class TeacherDetails(generic.UpdateView):
    model = models.Teacher
    form_class = forms.TeacherForm
    template_name = "object_edit/teacher_edit.html"
    template_name_suffix = '_update_form'
