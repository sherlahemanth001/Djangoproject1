from django.contrib import admin
from django.urls import path
from wcount import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views. home_view, name='home'),

]
