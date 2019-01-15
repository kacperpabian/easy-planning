from . import views
from django.urls import path, include
app_name = 'school_schedule'

urlpatterns = [
    # path('change-schedule/<int:pk>/', views.ScheduleChange.as_view(), name='schedule-change'),
    # path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete'),
    # path('add/', views.ScheduleCreate.as_view(), name='schedule-add'),
    path('create-school/', views.SchoolCreate.as_view(), name='school-create'),
    path('update-school/<int:pk>/', views.SchoolUpdate.as_view(), name='school-update'),
    path('del-school/<int:pk>/', views.SchoolDelete.as_view(), name='school-delete'),
    path('schedule/create-schedule/<int:pk>/', views.ScheduleCreate.as_view(), name='schedule-create'),
    path('subjects/', include('subjects.urls')),
    path('rooms/', include('rooms.urls')),
    path('teachers/', include('teachers.urls')),
    path('classes_templates/', include('classes_app.urls'))
]
