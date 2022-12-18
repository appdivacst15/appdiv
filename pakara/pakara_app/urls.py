from django.urls import path

from . import views


app_name = 'pakara_app'
urlpatterns = [
    path('collection/', views.CollectionView.as_view(), name="collection"),
    path('', views.IndexView.as_view(), name="index"),
]