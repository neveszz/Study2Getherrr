from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout', views.logoutPage, name='logout'),
    path("", views.home, name="home"),
    path('profile/<str:pk>/', views.userProfile, name='user_profile'),
    path('room/<str:pk>', views.room, name="room"),
    path('create_room/', views.createRoom, name="createroom"),
    path('delete_room/<int:pk>/', views.deleteRoom, name='deleteroom'),
    path('update_room/<int:pk>', views.updateRoom, name='update_room'),
    path('update_user/', views.update_user, name="update_user"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)