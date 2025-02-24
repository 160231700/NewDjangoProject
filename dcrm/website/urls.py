from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),


    #//// Start of user management////
    #Shows to a dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    #Links to the sign up page
    path("sign_up/", views.sign_up, name="sign_up"),
    #Allows users to login or out without additional urls. Ex: accounts/login/
    #Below also circumvents the need for additional views
    path("accounts/", include("django.contrib.auth.urls")),

    #//// End of user management////

    path("ticket/", views.ticket, name="ticket"),

    #Shows a page with information about the corporation
    path("information/", views.information, name="information")
]