from . import views
from django.urls import path

app_name = 'start_page'

urlpatterns = [
    path('register', views.UserFormView.as_view(), name='register'),
    path('', views.index, name='index'),
    # /schedule/scheduleid
    path('<int:schedule_id>/', views.detail, name='detail'),
    # /schedule/scheduleid/favorite
    path('<int:schedule_id>/favorite/', views.favorite, name='favorite')
]
