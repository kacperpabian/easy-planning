from . import views
from django.urls import path
app_name = 'object_creation'

urlpatterns = [
    path('change-schedule/<int:pk>/', views.ScheduleChange.as_view(), name='schedule-change'),
    path('delete-schedule/<int:pk>/', views.ScheduleDelete.as_view(), name='schedule-delete'),
    path('add/', views.ScheduleCreate.as_view(), name='schedule-add'),
    path('subjects/<int:pk>/', views.SubjectsView.as_view(), name='subjects'),
    path('subjects/add-subject/<int:pk>/', views.SubjectCreate.as_view(), name='subject-add'),
    path('subjects/del-subject/<int:pk>/', views.SubjectDelete.as_view(), name='subject-delete'),
    path('subjects/update-subject/<int:pk>/', views.SubjectUpdate.as_view(), name='subject-update'),
    path('rooms/<int:pk>/', views.RoomsView.as_view(), name='rooms'),
    path('rooms/create-room/<int:pk>/', views.RoomCreate.as_view(), name='room-create'),
    path('rooms/del-room/<int:pk>/', views.RoomDelete.as_view(), name='room-delete'),
    path('rooms/update-room/<int:pk>/', views.RoomUpdate.as_view(), name='room-update'),
    path('teachers/<int:pk>/', views.TeacherView.as_view(), name='teachers'),
    path('teachers/create-teacher/<int:pk>/', views.TeacherCreate.as_view(), name='teacher-create'),
    path('teachers/del-teacher/<int:pk>/', views.TeacherDelete.as_view(), name='teacher-delete'),
    path('teachers/update-teacher/<int:pk>/', views.TeacherUpdate.as_view(), name='teacher-update'),
    path('teachers/details-teacher/<int:pk>/', views.TeacherDetails.as_view(), name='teacher-details'),
    path('classes/<int:pk>/', views.ClassView.as_view(), name='classes'),
    path('classes/create-class/<int:pk>/', views.ClassCreate.as_view(), name='class-create'),
    path('classes/del-class/<int:pk>/', views.ClassDelete.as_view(), name='class-delete'),
    path('classes/update-class/<int:pk>/', views.ClassUpdate.as_view(), name='class-update'),
    path('classes/details-class/<int:pk>/', views.ClassDetails.as_view(), name='class-details')

]
