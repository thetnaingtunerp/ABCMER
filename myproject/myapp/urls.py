from django.urls import path
from .views import *
app_name = 'myapp'
urlpatterns = [
    path('', dashboard, name='dashboard'),  #dashboard
]