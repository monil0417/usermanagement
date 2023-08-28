from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user-list/', views.user_list_view, name='user-list'),
    path('edit-user/<int:user_id>/', views.edit_user_view, name='edit-user'),
    path('delete-user/<int:user_id>/', views.delete_user_view, name='delete-user'),
]
