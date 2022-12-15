from django.urls import path

from . import views


app_name = 'pakara_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]