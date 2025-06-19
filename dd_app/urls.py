from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.loginpage,name="login"),
    
    
    
    
    path('adminhome',views.adminhome,name="adminhome"),
    path('manage_staffs',views.manage_staffs,name="manage_staffs"),



    
]