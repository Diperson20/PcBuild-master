from django.core.management.base import BaseCommand
from django.urls.base import clear_url_caches

class ClearRouteCache(BaseCommand):
    help = 'Route Cache Clear'

    def handle(self, *args, **options):
        clear_url_caches()
        # Code to implement the functionality of your command goes here
        self.stdout.write('Route Cache Cleared!')
