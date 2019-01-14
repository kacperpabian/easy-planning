from . import views
from django.urls import path
app_name = 'classes_app'

urlpatterns = [
    path('<int:pk>/', views.ClassView.as_view(), name='classes'),
    path('create-class/<int:pk>/', views.ClassCreate.as_view(), name='class-create'),
    path('del-class/<int:pk>/', views.ClassDelete.as_view(), name='class-delete'),
    path('update-class/<int:pk>/', views.ClassUpdate.as_view(), name='class-update'),
    path('details-class/<int:pk>/', views.ClassDetails.as_view(), name='class-details')
]