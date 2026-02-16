from django.core.management.base import BaseCommand
from tickets.models import TicketEvent
from django.core.management import call_command


class Command(BaseCommand):
    help = "Seed database only if empty on docker start"

    def handle(self, *args, **kwargs):
        if not TicketEvent.objects.exists():
            call_command("seed")
        else:
            self.stdout.write("Database seeded")
