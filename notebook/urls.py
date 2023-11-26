from django.urls import path
from . import views

urlpatterns = [
    path("#", views.dashboard, name="dashboard"),
    path("login/", views.loginAccount, name="login"),
    path("logout/", views.logoutAccount, name="logout"),
    path("", views.notes, name="notes"),
]