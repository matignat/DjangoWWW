from django.urls import path
from . import views


urlpatterns = [
    # TODO: Add a path for "" (empty string = root) that calls views.home
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("greet/<str:name>/", views.greet, name="greet"),
    path("projects/", views.projects, name="projects"),
]