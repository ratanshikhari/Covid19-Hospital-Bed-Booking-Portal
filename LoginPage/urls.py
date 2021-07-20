from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginPage, name="loginPage"),
    url(r'^register$', views.registerPage, name="registerPage"),
]
