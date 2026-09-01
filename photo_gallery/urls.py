from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('photo/<int:pk>/dislike/', views.toggle_dislike, name='toggle_dislike'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] 