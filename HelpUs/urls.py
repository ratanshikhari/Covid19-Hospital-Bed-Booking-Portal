from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.HelpUs, name="HelpUs"),
]