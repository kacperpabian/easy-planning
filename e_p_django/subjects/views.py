from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django_tables2 import (
    SingleTableView,
    LazyPaginator
)

from .forms import SubjectForm
from .models import Subject
from .tables import SubjectTable
from e_p_django.schools.models import School


class SubjectsView(SingleTableView):
    model = Subject
    template_name = 'subjects/subjects.html'
    table_class = SubjectTable
    paginator_class = LazyPaginator

    def get_context_data(self, **kwargs):
        context = super(SubjectsView, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=self.kwargs.get('pk', ))
        return context

    def get_queryset(self):
        school = get_object_or_404(School, id=self.kwargs.get('pk', ))
        return Subject.objects.filter(school_id=school.id)


class SubjectCreate(generic.CreateView):
    model = Subject
    template_name = "subjects/subject_add.html"
    form_class = SubjectForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(SubjectCreate, self).form_valid(form)


class SubjectDelete(generic.DeleteView):
    model = Subject
    template_name = "subjects/subject_delete.html"

    # context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(SubjectDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(School, id=school_id)
        context['subject'] = get_object_or_404(Subject, id=self.kwargs.get('pk', ))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:schools:subjects:subjects', kwargs={'pk': school_id})


class SubjectUpdate(generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_edit.html"
    template_name_suffix = '_update_form'

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            if form.changed_data:
                obj = form.save(commit=False)
                obj.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")
        return render(request, self.template_name, {'form': form})
