from django.urls import path, include

from . import views
from e_p_django.schools.views import SchoolView


app_name = 'start_page'

urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('', SchoolView.as_view(), name='schools'),
    path('details/', include('schools.urls')),
    path('profile/', include('user_profile.urls'))
]
