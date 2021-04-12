from django.urls import path
from main.views import *


urlpatterns = [
    path('company/', CompanyCreateView.as_view()),
    path('device/', DeviceCreateView.as_view()),
    path('location/', LocationCreateView.as_view()),
]