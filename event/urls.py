from django.urls import path
from .views import *

app_name = "event"

urlpatterns = [
    path('event/', event_list, name='event_list'),
]
