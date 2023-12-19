from django.contrib import admin
from django.urls import path
from home_service.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('service',All_Service,name="service"),
    path('contact',contact,name="contact"),
    path('about',about,name="about"),
    path('login',Login_User,name="login"),
    path('admin_login',Login_admin,name="admin_login"),
    path('signup',Signup_User,name="signup"),
    path('search_cities',search_cities,name="search_cities"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)