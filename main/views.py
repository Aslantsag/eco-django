from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from main.models import *
from main.serializers import *


class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_class = permissions.IsAuthenticated


class DeviceCreateView(CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_class = permissions.IsAuthenticated


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_class = permissions.IsAuthenticated


class LocationRetrieveView(LoginRequiredMixin, TemplateView):
    template_name = "main/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = Location.objects.all()
        return context


