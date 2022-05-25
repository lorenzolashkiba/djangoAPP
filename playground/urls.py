from django.urls import path
from . import views

#URL conf module
urlpatterns = [
    path('hello/',views.say_hello)
]