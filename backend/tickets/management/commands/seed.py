from django.core.management.base import BaseCommand
from tickets.models import TicketEvent, TicketItem
from faker import Faker
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
import random

fake = Faker("it_IT")


class Command(BaseCommand):
    help = 'Events and tickets seeder - creates 200 random events with 10-30 tickets each'

    def add_arguments(self, parser):
        parser.add_argument(
            "--events",
            type=int,
            default=200
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.HTTP_INFO("Seeding events and tickets..."))
        events_created = 0
        tickets_created = 0
        total_events = options["events"]

        for _ in range(total_events):
            add_days = random.randint(0, 30)
            start_datetime = timezone.now() + timedelta(days=add_days)
            city = random.choice([
                "Roma",
                "Milano",
                "Napoli",
                "Torino",
                "Bologna",
                "Firenze",
                "Venezia",
                "Verona",
                "Palermo",
                "Bari",
            ])
            event_type = random.choice([
                "Concerto",
                "Festival",
                "Spettacolo teatrale",
                "Evento sportivo",
                "Stand-up comedy",
            ])
            venue = random.choice([
                "Stadio",
                "Forum",
                "Teatro",
                "Arena",
                "Palazzetto dello sport",
                "Auditorium"
            ])

            event = TicketEvent.objects.create(
                title=f"{event_type}",
                place=f"{venue} di {city} - {fake.address()}",
                city=city,
                start_datetime=start_datetime,
                end_datetime=start_datetime + timedelta(minutes=random.randint(30, 120))
            )
            events_created += 1

            for _ in range(random.randint(5, 7)):
                sector_prefix = chr(random.randint(ord('A'), ord('Z')))
                TicketItem.objects.create(
                    event=event,
                    price=Decimal(random.randint(20, 200)),
                    quantity=random.randint(1, 500),
                    section=fake.word(),
                    sector=f"{sector_prefix}{random.randint(1, 20)}",
                    row=str(random.randint(1, 30)),
                    seat=str(random.randint(1, 100)),
                    notes=fake.sentence(),
                )
                tickets_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Created {events_created} events and {tickets_created} tickets."
            )
        )
