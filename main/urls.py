from django.urls import path, include
from rest_framework.routers import SimpleRouter
from main.views import *


urlpatterns = [
    path('company/', CompanyCreateView.as_view()),
    path('device/', DeviceCreateView.as_view()),
    path('location/', LocationCreateView.as_view()),
    path('map/', LocationRetrieveView.as_view())
]