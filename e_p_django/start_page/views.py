from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserFormRegister, UserFormLogin
from . import models


class UserLoginView(generic.View):
    form_class = UserFormLogin
    template_name = 'start_page/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(None)
        username = ['username']
        password = ['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('start_page:index')

        return render(request, self.template_name, {'form': form})


class UserRegisterView(generic.View):
    form_class = UserFormRegister
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
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('start_page:index')

        return render(request, self.template_name, {'form': form})


class IndexView(generic.ListView):
    template_name = 'start_page/index.html'
    context_object_name = 'all_schedules'

    def get_queryset(self):
        return models.Schedule.objects.all()


class DetailView(generic.DetailView):
    model = models.Schedule
    template_name = "start_page/schedule_detail.html"


class ScheduleCreate(CreateView):
    model = models.Schedule
    fields = ['name', 'cycle', 'school_year', 'school_name', 'description', 'weekend_days', 'start_time',
              'max_lessons', 'user']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super(ScheduleCreate, self).form_valid(form)
