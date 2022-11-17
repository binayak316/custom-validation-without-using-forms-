from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('login-user', views.login_user, name = "login"),
    path('register-user', views.register, name = "register"),
    path('logout/', views.logout_user, name="logout"),
    
]