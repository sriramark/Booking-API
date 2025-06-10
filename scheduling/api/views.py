from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import filters
from django.utils import timezone

from scheduling.models import ScheduledClass, Booking
from .serializers import ScheduledClassListSerializer, BookingCreateSerializer, BookingDetailSerializer


class ScheduledClassListView(generics.ListAPIView):
    """
    API endpoint to list all upcoming fitness classes.
    Allows filtering by class type and searching across class title or instructor names.
    """
    serializer_class = ScheduledClassListSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['title', 'instructor__name']

    def get_queryset(self):
        queryset = ScheduledClass.objects.filter(datetime__gte=timezone.now()).order_by('datetime')

        # Filter by fitness class type (e.g., ?type=Yoga)
        class_type = self.request.query_params.get('type')
        if class_type:
            queryset = queryset.filter(fitness_class__name__iexact=class_type)

        return queryset.select_related('fitness_class')


class BookingCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new booking.
    Validates class availability and overbooking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer


class BookingListView(generics.ListAPIView):
    """
    API endpoint to list ALL bookings for a specific email address.
    Requires an 'email' query parameter.
    Example: GET /api/bookings/?email=user@example.com
    """
    serializer_class = BookingDetailSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')

        if not email:
            raise ValidationError({"email": "Email parameter is required to view bookings."})

        queryset = Booking.objects.filter(
            email__iexact=email,
        ).order_by('scheduled_class__datetime') 

        # Optimize queries for nested serializer's related data
        return queryset.select_related(
            'scheduled_class',
            'scheduled_class__fitness_class',
            'scheduled_class__fitness_class__instructor'
        )

