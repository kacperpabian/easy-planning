from django.urls import path

from . import views
app_name = 'lessons_panel'

urlpatterns = [
    path('<int:pk>/', views.LessonsPanelView.as_view(), name='lessons-panel'),
    path('ajax/load-schedules/', views.load_schedules, name='ajax_load_schedules'),
    path('ajax/load-schedule-panel/', views.load_schedule_panel, name='ajax_load_schedule_panel'),
    path('del-lesson/<int:pk>/', views.LessonDelete.as_view(), name='lesson_delete')
    # path('selected-class/<int:pk>/', views.SelectClass.as_view(), name='selected-class')
]
