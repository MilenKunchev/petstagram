from django.urls import path

from petstagram.main.views import show_home

urlpatterns = (
    path('', show_home, name='index'),
)

