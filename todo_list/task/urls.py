from django.urls import path
from. views import main, update_task, delete_task


urlpatterns = [
    path('', main, name='home'),
    path('update/<str:pk>/', update_task, name='update' ),
    path('delete/<str:pk>/', delete_task, name='delete')
]