from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'), #Empty string '' means it matches the root URL, ex: http://example.com/
]