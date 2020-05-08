from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login-page'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='user-register'),
    path('my-profile/', views.myProfile, name='user-my-profile'),
    path('experience/', views.experience, name='user-experience'),
    path('education/', views.education, name='user-education'),
    path('detail/', views.userDetail, name='user-detail'),
]
