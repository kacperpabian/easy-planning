from . import views
from django.urls import path
app_name = 'subjects'

urlpatterns = [
    path('<int:pk>/', views.SubjectsView.as_view(), name='subjects'),
    path('add-subject/<int:pk>/', views.SubjectCreate.as_view(), name='subject-add'),
    path('del-subject/<int:pk>/', views.SubjectDelete.as_view(), name='subject-delete'),
    path('update-subject/<int:pk>/', views.SubjectUpdate.as_view(), name='subject-update'),
]