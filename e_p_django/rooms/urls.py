from . import views
from django.urls import path
app_name = 'rooms'

urlpatterns = [
    path('<int:pk>/', views.RoomsView.as_view(), name='rooms'),
    path('create-room/<int:pk>/', views.RoomCreate.as_view(), name='room-create'),
    path('del-room/<int:pk>/', views.RoomDelete.as_view(), name='room-delete'),
    path('update-room/<int:pk>/', views.RoomUpdate.as_view(), name='room-update'),
]