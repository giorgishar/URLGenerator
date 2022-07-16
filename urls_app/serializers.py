from django.http import QueryDict
from rest_framework import serializers

from urls_app.models import URL


class URLCreateSerializer(serializers.ModelSerializer):
    visited_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = URL
        fields = ['name', 'visited_count']

    def create(self, validated_data):
        return URL.objects.create(
            user=self.context['request'].user,
            **validated_data
        )


class URLFreemiumCreateSerializer(URLCreateSerializer):
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return URL.objects.create(
            user=self.context['request'].user,
            name=URL.generate_random_unique_name()
        )
