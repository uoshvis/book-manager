from django.urls import path

from . import views


urlpatterns = [

    path("<int:pk>/", views.author_detail, name="author_detail"),

]
