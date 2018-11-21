from . import views
from django.urls import path
app_name = 'object_creation'

urlpatterns = [
    path('', views.SubjectView.as_view(), name='subjects')
]
