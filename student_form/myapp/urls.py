from django.urls import path
from .views import index, login_view, signup,main

urlpatterns = [
    path('', index, name='home'),
    path('login/',login_view, name='login'),
    path('signup/', signup, name='signup' ),
    path('main/', main, name='main')
]