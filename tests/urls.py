from django.urls import include, path

urlpatterns = [
    path("publications/", include("publications.urls")),
]