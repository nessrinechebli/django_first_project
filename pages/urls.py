from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
