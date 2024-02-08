from django.urls import path
from . import views

urlpatterns = [
    path('password-list/', views.password_list, name='password_list'),
    path('add-password/', views.add_password, name='add_password'),
    path('edit-password/', views.edit_password, name='edit_password'),
    path('delete-password/<int:pk>/', views.delete_password, name='delete_password'),
]

