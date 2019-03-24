from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages

import logging

from . import models
from . import forms
from django.urls import reverse_lazy


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


# class BreakesScheduleCreate(generic.TemplateView):
logger = logging.getLogger(__name__)


class SchoolView(generic.TemplateView):
    model = models.School
    template_name = 'schools/schools.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['all_schools'] = models.School.objects.filter(user=user.id)
        # context['schedule_table'] = models.Schedule.objects.filter()
        return context

    # def get_queryset(self):
    #     user = self.request.user
    #     return models.School.objects.filter(user=user.id)


class SchoolCreate(generic.CreateView):
    model = models.School
    template_name = 'schools/school_add.html'
    form_class = forms.SchoolForm

    def form_valid(self, form):
        self.form_save(form)
        return super(SchoolCreate, self).form_valid(form)

    def form_save(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.user_id = self.request.user.id
        return obj


# class SchoolCreate(generic.TemplateView):
#     # model = models.School
#     template_name = 'schools/school_add.html'
#     school_form_class = forms.SchoolForm
#     # breakes_form_class = forms.SchoolBreakesForm
#
#     def post(self, request):
#         post_data = request.POST or None
#         school_form = self.school_form_class(post_data, prefix='school_form')
#         # breakes_form = self.breakes_form_class(post_data, prefix='breakes_form')
#
#         # context = self.get_context_data(school_form=school_form, breakes_form=breakes_form)
#         context = self.get_context_data(school_form=school_form)
#
#         if school_form.is_valid():
#             self.form_save(school_form)
#         # if breakes_form.is_valid():
#         #     self.form_save(breakes_form)
#
#         return self.render_to_response(context)

    # def form_save(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     logger.error('\n\n\n@@@@@@@@@@@@@@@@USER ID@@@@@@@@@@@@@@@@ ' + str(obj.user_id))
    #     messages.success(self.request, "{} saved successfully".format(obj))
    #     return obj
    #
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.created_by = self.request.user
    #     obj.user_id = self.request.user.id
    #     return super(SchoolCreate, self).form_valid(form)


class SchoolUpdate(generic.UpdateView):
    form_class = forms.SchoolForm
    template_name = 'schools/school_edit.html'
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
    template_name = "schools/school_delete.html"
    success_url = reverse_lazy('start_page:schools')



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
