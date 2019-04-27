from django.urls import path

from . import views
app_name = 'lessons_panel'

urlpatterns = [
    path('<int:pk>/', views.LessonsPanelView.as_view(), name='lessons-panel'),
    # path('selected-class/<int:pk>/', views.SelectClass.as_view(), name='selected-class')
]
