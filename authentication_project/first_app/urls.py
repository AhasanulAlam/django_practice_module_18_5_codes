
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('signup/', views.signup, name='signup_page'),
    path('login/', views.user_login, name='login_page'),
    path('logout/', views.user_logout, name='logout_page'),
    path('pass_change/', views.pass_change, name='pass_change_page'),
    path('pass_change2/', views.pass_change_without_old, name='pass_change_without_old_page'),
    path('profile/', views.profile, name='profile_page'),
]
