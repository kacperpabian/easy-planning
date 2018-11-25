from . import views
from django.urls import path
app_name = 'object_creation'

urlpatterns = [
    path('change-schedule/<int:pk>/', views.ScheduleChange.as_view(), name='schedule-change'),
    path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete')
]
