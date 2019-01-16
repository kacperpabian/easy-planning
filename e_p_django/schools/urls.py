from . import views
from django.urls import path, include
app_name = 'schools'

urlpatterns = [
    # path('change-schedule/<int:pk>/', views.ScheduleChange.as_view(), name='schedule-change'),
    # path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete'),
    # path('add/', views.ScheduleCreate.as_view(), name='schedule-add'),
    path('create-school/', views.SchoolCreate.as_view(), name='school-create'),
    path('update-school/<int:pk>/', views.SchoolUpdate.as_view(), name='school-update'),
    path('del-school/<int:pk>/', views.SchoolDelete.as_view(), name='school-delete'),
    path('schedules/', include('schedules.urls')),
    path('subjects/', include('subjects.urls')),
    path('rooms/', include('rooms.urls')),
    path('teachers/', include('teachers.urls')),
    path('classes/', include('classes_app.urls')),
    path('lessons_panel/', include('lessons_panel.urls'))
]
