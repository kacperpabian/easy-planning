from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user, get_user_model
from django.views import generic
from .forms import UserFormRegister, UserFormLogin
# noinspection PyUnresolvedReferences
from object_creation.forms import ScheduleForm
from . import models


class UserLoginView(generic.View):
    """View for user login"""
    form_class = UserFormLogin
    template_name = 'registration/home.html'

    def get(self, request):
        form = self.form_class()
        user = get_user(request)
        if user.is_authenticated:
            return redirect('start_page:schedules')
        else:
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.POST.get('submit') == 'sign-in':
            form = self.form_class()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('start_page:schedules')
            else:
                messages.error(request, "Błędny login bądź hasło")

            return render(request, self.template_name, {'form': form})
        elif request.POST.get('submit') == 'sign-up':
            return redirect('start_page:register')


class UserRegisterView(generic.View):
    """View for user registration"""
    form_class = UserFormRegister
    template_name = 'registration/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        email = request.POST['email']
        if models.AuthUser.objects.filter(email=email):
            messages.error(request, "Użytkownik z takim adresem email już istnieje.")
        elif form.is_valid():
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
                    return redirect('start_page:schedules')

        return render(request, self.template_name, {'form': form})


class ScheduleView(generic.ListView):
    model = models.Schedule
    template_name = 'start_page/schedules.html'
    context_object_name = 'all_schedules'

    def get_queryset(self):
        user = self.request.user
        return models.Schedule.objects.filter(user_id=user.id)
