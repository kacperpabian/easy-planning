from . import views
from django.urls import path, include
app_name = 'user_profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile')
]

