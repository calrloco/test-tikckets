from .serializers import TicketEventSerializer
from rest_framework.generics import ListAPIView
from .models import TicketEvent
from django.utils import timezone
from django.db.models import Q


class EventListAPIView(ListAPIView):
    serializer_class = TicketEventSerializer

    def get_queryset(self):
        params = self.request.query_params
        q = params.get("q", "").strip()
        base_query = (TicketEvent.objects
                      .prefetch_related("ticket_items")
                      .filter(start_datetime__gte=timezone.now()))
        if q:
            base_query = base_query.filter(Q(city__contains=q) | Q(title__contains=q))

        return base_query.order_by("-start_datetime")
