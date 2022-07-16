from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from urls_app.models import URL
from urls_app.serializers import URLCreateSerializer, URLFreemiumCreateSerializer
from users.permissions import IsPremium


class URLCreateAPIView(ModelViewSet):
    http_method_names = ['post', 'get']
    serializer_class = URLCreateSerializer
    permission_classes = [IsPremium]
    lookup_field = 'name'

    def get_object(self):
        obj: URL = super().get_object()
        obj.increase_visited_count()
        return obj

    def get_queryset(self):
        return URL.objects.filter(user=self.request.user)


class URLCreateFreemiumAPIView(URLCreateAPIView):
    serializer_class = URLFreemiumCreateSerializer
    permission_classes = [IsAuthenticated]
