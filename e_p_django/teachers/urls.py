from . import views
from django.urls import path
app_name = 'teachers'

urlpatterns = [
    path('<int:pk>/', views.TeacherView.as_view(), name='teachers'),
    path('create-teacher/<int:pk>/', views.TeacherCreate.as_view(), name='teacher-create'),
    path('del-teacher/<int:pk>/', views.TeacherDelete.as_view(), name='teacher-delete'),
    path('update-teacher/<int:pk>/', views.TeacherUpdate.as_view(), name='teacher-update'),
    path('details-teacher/<int:pk>/', views.TeacherDetails.as_view(), name='teacher-details'),
]