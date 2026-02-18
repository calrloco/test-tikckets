from .serializers import TicketEventSerializer
from rest_framework.generics import ListAPIView
from .models import TicketEvent
from django.utils import timezone
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class EventListAPIView(ListAPIView):
    serializer_class = TicketEventSerializer

    def get_queryset(self):
        params = self.request.query_params
        search = params.get("q", "").strip()

        query = (TicketEvent.objects
                 .prefetch_related("ticket_items")
                 .filter(start_datetime__gte=timezone.now()))

        if search:
            vector = SearchVector("title", "city", config="italian")
            search_query = SearchQuery(search, config="italian", search_type="websearch")

            query = query.annotate(search_vector=vector)
            query = query.filter(search_vector=search_query)
            query = query.annotate(rank=SearchRank("search_vector", search_query))

            return query.filter(rank__gte=0.05).order_by("-rank", "-start_datetime")

        return query.order_by("-start_datetime")
