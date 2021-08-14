from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]
