from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .forms import UserForm
from . import models
from . import serializers
from . import permissions


class UserViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.AuthUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks password and returns auth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create token"""
        return ObtainAuthToken().post(request)


class UserFormView(generic.View):
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
            # store locally yet not post to database
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            # returns User object if credentials are correct
            user = authenticate(request, username=username, password=password)
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


class ScheduleUpdate(UpdateView):
    model = models.Schedule
    fields = ['name', 'cycle', 'school_year', 'school_name', 'description', 'weekend_days', 'start_time',
              'max_lessons', 'user']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ScheduleDelete(DeleteView):
    model = models.Schedule
    success_url = reverse_lazy('start_page:index')
