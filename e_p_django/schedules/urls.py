from django.urls import path

from . import views
app_name = 'schedules'

urlpatterns = [
    path('create-schedule/<int:pk>/', views.ScheduleCreate.as_view(), name='schedule-create'),
]
