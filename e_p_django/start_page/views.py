from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import HttpResponse
from django.template import loader
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
    template = loader.get_template('start_page/index.html')
    context = {
        'all_schedules': all_schedules,
    }
    return HttpResponse(template.render(context, request))


def detail(request, schedule_id):
    return HttpResponse("<h2>Details for Schedule id: " + str(schedule_id) + "</h2>")
