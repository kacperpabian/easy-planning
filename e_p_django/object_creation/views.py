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


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


# class BreakesScheduleCreate(generic.TemplateView):


class SchoolCreate(generic.TemplateView):
    # model = models.School
    template_name = 'object_creation/school_add.html'
    school_form_class = forms.SchoolForm
    breakes_form_class = forms.SchoolBreakesForm

    def post(self, request):
        post_data = request.POST or None
        school_form = self.school_form_class(post_data, prefix='school_form')
        breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')

        context = self.get_context_data(school_form=school_form, breakes_form=breakes_form)

        if school_form.is_valid():
            self.form_save(school_form)
        if breakes_form.is_valid():
            self.form_save(breakes_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        obj.created_by = self.request.user
        obj.user_id = self.request.user.id
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     return super(SchoolCreate, self).form_valid(form)


class SchoolUpdate(generic.UpdateView):
    form_class = forms.SchoolForm
    template_name = 'object_edit/school_edit.html'
    template_name_suffix = '_update_form'

    def get_queryset(self):
        user = self.request.user
        return models.School.objects.filter(user_id=user.id)

    # display blank form
    def get(self, request, **kwargs):
        schedule = self.get_object()
        data = {'cycle': schedule.cycle,
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
                obj = form.save(commit=False)
                obj.save()
                messages.success(request, "Pomyślnie zaktualizowano informacje")
            else:
                messages.warning(request, "Nic nie zostało zmienione.")

        return render(request, self.template_name, {'form': form})


class SchoolDelete(generic.DeleteView):
    model = models.School
    template_name = "object_delete/school_delete.html"
    success_url = reverse_lazy('start_page:schools')


class ScheduleCreate(generic.CreateView):
    model = models.Schedule
    template_name = "object_creation/schedule_add.html"
    form_class = forms.ScheduleForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.school_id = self.kwargs['pk']
        return super(ScheduleCreate, self).form_valid(form)


class ScheduleDelete(generic.DeleteView):
    model = models.Schedule
    template_name = "object_delete/schedule_delete.html"

    # context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        school_id = self.object.school_id
        context = super(ScheduleDelete, self).get_context_data(**kwargs)
        context['school'] = get_object_or_404(models.School, id=school_id)
        context['schedule'] = get_object_or_404(models.Schedule, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        school_id = self.object.school_id
        return reverse_lazy('start_page:schools', kwargs={'pk': school_id})


# class ScheduleChange(generic.UpdateView):
#     form_class = forms.ScheduleForm
#     template_name = 'object_edit/schedule_edit.html'
#     template_name_suffix = '_update_form'
#
#     def get_queryset(self):
#         user = self.request.user
#         return models.Schedule.objects.filter(user_id=user.id)
#
#     # display blank form
#     def get(self, request, **kwargs):
#         schedule = self.get_object()
#         data = {'name': schedule.name,
#                 'cycle': schedule.cycle,
#                 'school_year': schedule.school_year,
#                 'school_name': schedule.school_name,
#                 'description': schedule.description,
#                 'weekend_days': schedule.weekend_days,
#                 'start_time': schedule.start_time,
#                 'max_lessons': schedule.max_lessons}
#         form = self.form_class(initial=data)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, **kwargs):
#         form = self.form_class(request.POST, instance=self.get_object())
#         if form.is_valid():
#             if form.changed_data:
#                 schedule = form.save(commit=False)
#                 schedule.save()
#                 messages.success(request, "Pomyślnie zaktualizowano informacje")
#             else:
#                 messages.warning(request, "Nic nie zostało zmienione.")
#
#         return render(request, self.template_name, {'form': form})


# class ScheduleDelete(generic.DeleteView):
#     model = models.Schedule
#     template_name = "object_delete/schedule_delete.html"
#     success_url = reverse_lazy('start_page:schedules')
