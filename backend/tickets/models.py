from django.db import models


class TicketEvent(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        db_table = "ticket_event"
        indexes = [
            models.Index(fields=["city"]),
            models.Index(fields=["title"]),
        ]


class TicketItem(models.Model):
    event = models.ForeignKey(
        TicketEvent,
        related_name="ticket_items",
        on_delete=models.CASCADE,
        db_column="event_id",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    section = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    row = models.CharField(max_length=255)
    seat = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "ticket_item"
        indexes = [
            models.Index(fields=["price"]),
        ]
