from django.urls import path

from . import views
app_name = 'credentials'
# here we going to views using path and function
urlpatterns = [

    path('register/', views.register, name='rregister'),
    path('login/',views.login,name='rlogin'),
    path('logout/',views.logout,name='rlogout'),
]
