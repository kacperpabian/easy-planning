from django.urls import path

from . import views
app_name = 'lessons_panel'

urlpatterns = [
    path('<int:pk>/', views.LessonsPanelView.as_view(), name='lessons-panel'),
]
