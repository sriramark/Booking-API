from django.contrib import admin

from .models import ScheduledClass, Booking

@admin.register(ScheduledClass)
class ScheduledClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'total_available_slots', 'available_slots', 'is_full', 'instructor')
    search_fields = ('title', 'fitness_class__name', 'instructor__name',)
    list_filter = ('datetime', 'instructor__name', 'fitness_class__name',)
    readonly_fields = ('available_slots', 'is_full')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'scheduled_class', 'booking_time',)
    search_fields = ('name', 'email', 'scheduled_class__title')
    list_filter = ('booking_time', )
    raw_id_fields = ('scheduled_class',)
