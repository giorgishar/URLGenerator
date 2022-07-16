import datetime

from django.core.management import BaseCommand
from django.utils import timezone

from urls_app.models import URL


class Command(BaseCommand):
    def handle(self, *args, **options):
        URL.objects.filter(created_date__gte=timezone.now() - datetime.timedelta(days=30)) \
            .delete()
