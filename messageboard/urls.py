from django.urls import path

from .views import homePageView, addView, removeView, searchView, registerView

urlpatterns = [
    path('', homePageView, name='home'),
    path('add/', addView, name='add'),
    path('remove/', removeView, name='add'),
    path('search/', searchView, name='search'),
    path('login/register/', registerView, name='register'),
]