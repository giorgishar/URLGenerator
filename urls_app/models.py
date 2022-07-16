import random

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.conf import settings


class URL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.SlugField(max_length=249, unique=True, validators=[MinLengthValidator(8)])
    visited_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def increase_visited_count(self) -> None:
        self.visited_count += 1
        self.save()

    @staticmethod
    def generate_random_unique_name() -> str:
        name: str
        while True:
            name = slugify(get_random_string(length=random.randint(8, 249)))

            if URL.objects.filter(name=name).exists():
                continue

            return name
