from . import views
from django.urls import path

app_name = 'start_page'

urlpatterns = [
    path('register', views.UserFormView.as_view(), name='register'),
    path('', views.IndexView.as_view(), name='index'),
    # /schedule/scheduleid
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /schedules/schedule/add/
    path('schedule/add/', views.ScheduleCreate.as_view(), name='schedule-add')

]
