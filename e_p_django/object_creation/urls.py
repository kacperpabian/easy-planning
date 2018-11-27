from . import views
from django.urls import path
app_name = 'object_creation'

urlpatterns = [
    path('change-schedule/<int:pk>/', views.ScheduleChange.as_view(), name='schedule-change'),
    path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete'),
    path('subjects/<int:pk>/', views.SubjectsView.as_view(), name='subjects'),
    path('subjects/add-subject/<int:pk>/', views.SubjectCreate.as_view(), name='subject-add'),
    path('subjects/del-subject/<int:pk>/', views.SubjectDelete.as_view(), name='subject-delete'),
    path('subjects/update-subject/<int:pk>/', views.SubjectUpdate.as_view(), name='subject-update')
]
