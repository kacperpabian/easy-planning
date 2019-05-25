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
    path('schedules/', include('e_p_django.schedules.urls')),
    path('subjects/', include('e_p_django.subjects.urls')),
    path('rooms/', include('e_p_django.rooms.urls')),
    path('teachers/', include('e_p_django.teachers.urls')),
    path('classes/', include('e_p_django.classes_app.urls')),
    path('lessons-panel/', include('e_p_django.lessons_panel.urls'))
]
