from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from . import models


class UserFormView(View):
    form_class = UserForm
    template_name = 'start_page/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            passsword = form.cleaned_data['password']
            user.set_password(passsword)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, passsword=passsword)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('start_page:index')

        return render(request, self.template_name, {'form': form})


def index(request):
    all_schedules = models.Schedule.objects.all()
    return render(request, 'start_page/index.html', context={'all_schedules': all_schedules})


def detail(request, schedule_id):
    schedule = get_object_or_404(models.Schedule, id=schedule_id)
    return render(request, "start_page/schedule_detail.html", context={'schedule': schedule})


def favorite(request, schedule_id):
    schedule = get_object_or_404(models.Schedule, id=schedule_id)
    try:
        selected_subject = schedule.subject_set.get(id=request.POST['subject'])
    except (KeyError, models.Subject.DoesNotExist):
        return render(request, 'start_page/schedule_detail.html', context={
            'schedule': schedule,
            'error_message': "You did not select a valid subject"
      })
    else:
        if selected_subject.is_favorite:
            selected_subject.is_favorite = False
        else:
            selected_subject.is_favorite = True
        selected_subject.save()
        return render(request, 'start_page/schedule_detail.html', context={'schedule': schedule})
