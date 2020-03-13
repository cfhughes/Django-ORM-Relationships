from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('users/new',views.register,name='register'),
    path('users',views.list,name='list')
]