from django.urls import path
from App_UserLog import views

app_name = 'App_UserLog'

urlpatterns = [
    path('log/', views.user_log, name='userlog'),
  
]