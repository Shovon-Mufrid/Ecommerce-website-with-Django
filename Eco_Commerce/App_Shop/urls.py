from django.urls import path
from App_Shop import views
app_name = 'App_Shops'

urlpatterns = [
    path('', views.Home.as_view(), name='home' ),
    
]