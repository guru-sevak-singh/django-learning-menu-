from django.urls import path
from . import views
from django.contrib.auth import views as authontication_views 


app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', authontication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authontication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile_page, name='profile'),
]
