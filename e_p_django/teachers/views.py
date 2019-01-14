from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django_tables2 import (
    SingleTableView,
    LazyPaginator
)

from .forms import TeacherForm
from .models import Teacher
from .tables import TeacherTable
from start_page.models import School


class TeacherCreate(generic.CreateView):
    model = Teacher
    template_name = "teachers/teacher_add.html"
    form_class = TeacherForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(TeacherCreate, self).form_valid(form)


class TeacherView(SingleTableView):
    model = Teacher
    template_name = 'teachers/teachers.html'
    table_class = TeacherTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        school = get_object_or_404(School, id=self.kwargs.get('pk'))
        return Teacher.objects.filter(school_id=school.id)


class TeacherDelete(generic.DeleteView):
    model = Teacher
    template_name = "teachers/teacher_delete.html"

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(TeacherDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['teacher'] = get_object_or_404(Teacher, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:object_creation:teachers:teachers', kwargs={'pk': school_id})


class TeacherUpdate(generic.UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teachers/teacher_edit.html"
    template_name_suffix = '_update_form'

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if form.changed_data:
                teacher = form.save(commit=False)
                teacher.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")
        return render(request, self.template_name, {'form': form})


class TeacherDetails(generic.UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teachers/teacher_edit.html"
    template_name_suffix = '_update_form'
