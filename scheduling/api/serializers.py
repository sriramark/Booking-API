from rest_framework import serializers
from django.utils import timezone

from scheduling.models import ScheduledClass, Booking


class ScheduledClassListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing ScheduledClass objects in a flat structure for list UI display.
    """
    fitness_class_name = serializers.CharField(source='fitness_class.name', read_only=True)
    instructor_name = serializers.CharField(source='instructor.name', read_only=True)

    class Meta:
        model = ScheduledClass
        fields = ('id', 'title', 'datetime', 'total_available_slots', 'available_slots', 'is_full', 'fitness_class_name', 'instructor_name')


class BookingCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new Booking instances.
    Includes validation for class availability and past dates.
    """
    class Meta:
        model = Booking
        fields = ('scheduled_class', 'name', 'email')

    def validate(self, attrs):
        scheduled_class = attrs.get('scheduled_class')
        email = attrs.get('email')

        if scheduled_class.is_full:
            raise serializers.ValidationError("This class is fully booked.")
        if scheduled_class.datetime < timezone.now():
            raise serializers.ValidationError("Cannot book past classes.")

        # Prevent double booking at the same time for the same user
        if Booking.objects.filter(
            email=email,
            scheduled_class__datetime=scheduled_class.datetime
        ).exists():
            raise serializers.ValidationError("You already have a booking at this time.")

        return attrs


class BookingDetailSerializer(serializers.ModelSerializer):
    class ScheduledClassSerializer(serializers.ModelSerializer):
        fitness_class_name = serializers.CharField(source='fitness_class.name', read_only=True)
        instructor_name = serializers.CharField(source='fitness_class.instructor.name', read_only=True)

        class Meta:
            model = ScheduledClass
            fields = ('id', 'title', 'datetime', 'fitness_class_name', 'instructor_name')

    scheduled_class = ScheduledClassSerializer(read_only=True)
    is_past_booking = serializers.BooleanField(source='is_past', read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'name', 'email', 'booking_time', 'scheduled_class', 'is_past_booking')

