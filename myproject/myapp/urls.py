from django.urls import path
from .views import *
app_name = 'myapp'
urlpatterns = [
    path('login', UserLoginView.as_view(), name = 'UserLoginView'),
    path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('', dashboard, name='dashboard'),  #dashboard
    path('DashboardView/', DashboardView.as_view(), name='DashboardView'),
    path('data_entry/', data_entry.as_view(), name='data_entry'),
    path('mer_report/', mer_report.as_view(), name='mer_report'),
]