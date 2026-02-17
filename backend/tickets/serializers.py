from rest_framework import serializers

from .models import TicketEvent, TicketItem


class TicketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketItem
        fields = ["id", "price", "quantity", "section", "sector", "row", "seat", "notes"]


class TicketEventSerializer(serializers.ModelSerializer):
    ticket_items = TicketItemSerializer(many=True, read_only=True)

    class Meta:
        model = TicketEvent
        fields = ["id", "title", "place", "city", "start_datetime", "end_datetime", "ticket_items"]
