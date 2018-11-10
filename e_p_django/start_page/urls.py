from . import views
from django.urls import path, include

app_name = 'start_page'

urlpatterns = [
    path('register', views.UserFormView.as_view(), name='register')
]
