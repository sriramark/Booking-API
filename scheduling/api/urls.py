from django.urls import path
from .views import ScheduledClassListView, BookingCreateView, BookingListView

urlpatterns = [
    path('', ScheduledClassListView.as_view(), name='scheduled-class-list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
    path('bookings/', BookingListView.as_view(), name='booking-list'), 
]

