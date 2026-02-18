from rest_framework import serializers
from django.utils.formats import date_format
from .models import TicketEvent, TicketItem


class TicketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketItem
        fields = ["id", "price", "quantity", "section", "sector", "row", "seat", "notes"]


class TicketEventSerializer(serializers.ModelSerializer):
    ticket_items = TicketItemSerializer(many=True, read_only=True)
    start_datetime = serializers.SerializerMethodField()

    def get_start_datetime(self, obj):
        return date_format(obj.start_datetime, "j F Y H:i", use_l10n=True)

    class Meta:
        model = TicketEvent
        fields = ["id", "title", "place", "city", "start_datetime", "end_datetime", "ticket_items"]
