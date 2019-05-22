from django.urls import path

from . import views
app_name = 'schedules'

urlpatterns = [
    path('<int:pk>/', views.ScheduleView.as_view(), name='schedules'),
    path('create-schedule/<int:pk>/', views.ScheduleCreate.as_view(), name='schedule-create'),
    path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete'),
    path('update-schedule/<int:pk>/', views.ScheduleUpdate.as_view(), name='schedule-update'),
]
