from . import views
from django.urls import path, include

from rest_framework.routers import DefaultRouter

app_name = 'start_page'
router = DefaultRouter()
router.register('profile', views.UserViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    path('router', include(router.urls)),
    # /schedule
    path('', views.IndexView.as_view(), name='index'),
    # /schedule/register
    path('register', views.UserFormView.as_view(), name='register'),
    # /schedule/scheduleid
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /schedules/schedule/add/
    path('schedule/add/', views.ScheduleCreate.as_view(), name='schedule-add'),
    # /schedules/schedule/2/
    path('schedule/<int:pk>/', views.ScheduleUpdate.as_view(), name='schedule-update'),
    # /schedules/schedule/2/delete/
    path('schedule/<int:pk>/delete/', views.ScheduleDelete.as_view(), name='schedule-delete')

]
