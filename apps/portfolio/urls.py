from django.urls import path
from apps.portfolio import views


urlpatterns = [
    path('', views.HomeView.index, name='home'),
]
