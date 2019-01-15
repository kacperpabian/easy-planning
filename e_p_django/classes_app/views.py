from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django_tables2 import (
    SingleTableView,
    LazyPaginator
)


from .forms import ClassForm
from .models import Class
from .tables import ClassTable
from school_schedule.models import School


class ClassCreate(generic.CreateView):
    model = Class
    template_name = "classes_templates/class_add.html"
    form_class = ClassForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(ClassCreate, self).form_valid(form)


class ClassView(SingleTableView):
    model = Class
    template_name = 'classes_templates/classes.html'
    table_class = ClassTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(ClassView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        school = get_object_or_404(School, id=self.kwargs.get('pk'))
        return Class.objects.filter(school_id=school.id)


class ClassDelete(generic.DeleteView):
    model = Class
    template_name = "classes_templates/class_delete.html"

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(ClassDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['class'] = get_object_or_404(Class, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:school_schedule:classes_app:classes', kwargs={'pk': school_id})


class ClassUpdate(generic.UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "classes_templates/class_edit.html"
    template_name_suffix = '_update_form'

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if form.changed_data:
                classs = form.save(commit=False)
                classs.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")
        return render(request, self.template_name, {'form': form})


class ClassDetails(generic.UpdateView):
    model = Class
    form_class = ClassForm
    template_name = "classes_templates/class_edit.html"
    template_name_suffix = '_update_form'
