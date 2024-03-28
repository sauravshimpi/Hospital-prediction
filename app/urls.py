from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name= "home"),
    path("log_in", views.log_in, name= "log_in"),
    path("register", views.register, name= "register"),
    path("dashboard", views.dashboard, name= "dashboard"),
    path("non_mri", views.non_mri, name= "non_mri"),
    path("result_non_mri", views.result_non_mri, name= "result_non_mri"),
    path("log_out", views.log_out, name= "log_out"),
]