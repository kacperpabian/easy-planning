from django.urls import path, include

from . import views
app_name = 'start_page'

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('', views.SchoolView.as_view(), name='schools'),
    path('details/', include('object_creation.urls')),
    path('profile/', include('user_profile.urls'))
]
