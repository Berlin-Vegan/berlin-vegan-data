from django.core.management.base import BaseCommand

from bvdata.data.review_sync import import_reviews_from_wordpress


class Command(BaseCommand):
    help = "Import or updates reviews"

    def handle(self, *args, **options):
        import_reviews_from_wordpress()
        self.stdout.write(
            self.style.SUCCESS("Successfully all review imported or updated")
        )
