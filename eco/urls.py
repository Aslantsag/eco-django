from django.contrib import admin
from django.urls import path, include

from main.views import LocationRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', LocationRetrieveView.as_view())
]