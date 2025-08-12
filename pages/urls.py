from django.urls import path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about") #Specified the path to load the about page
]
