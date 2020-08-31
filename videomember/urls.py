from django.urls import path
from .import views
app_name = 'videomember'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('loginAccess/', views.UserAccess, name = 'loginAccess'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('lesson/<int:id>', views.lesson, name = 'lesson'),
]
