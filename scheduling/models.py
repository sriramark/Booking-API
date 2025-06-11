from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

from fitness_class.models import FitnessClass
from fitness_class.models import Instructor

class ScheduledClass(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE, related_name='scheduled_classes')
    title = models.CharField(max_length=200, help_text="Title of the current sesssion")  
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, related_name='classes')  
    datetime = models.DateTimeField()
    total_available_slots = models.PositiveIntegerField()

    class Meta:
        unique_together = ('instructor', 'datetime')
        ordering = ['datetime']

    @property
    def available_slots(self):
        return max(0, self.total_available_slots - self.bookings.count()) 
    
    @property
    def is_full(self):
        return self.available_slots == 0
    
    def save(self, *args, **kwargs):
        self.datetime = self.datetime.replace(second = 0, microsecond=0) # Remove seconds and microseconds for consistency
       
        # Enforce 30-minute gap between instructor's other classes
        start_window = self.datetime - timedelta(minutes=30)
        end_window = self.datetime + timedelta(minutes=30)
        
        overlapping_classes = ScheduledClass.objects.filter(
            instructor=self.instructor,
            datetime__range=(start_window, end_window)
        ).exclude(pk=self.pk)

        if overlapping_classes.exists():
            raise ValidationError(f"{self.instructor.name} already has a class within 30 minutes of this time.")
       
        fitness_class_instructors = self.fitness_class.instructors.all()
        if self.instructor not in fitness_class_instructors:
            raise ValidationError("Instructor must be one of the instructors for the fitness class.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} on {self.datetime.strftime('%Y-%m-%d %H:%M')}"


class Booking(models.Model):
    scheduled_class = models.ForeignKey(ScheduledClass, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    booking_time = models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together = ('scheduled_class', 'email') # Ensures a user can only book one slot for a scheduled class
        ordering = ['booking_time']

    @property
    def is_past(self):
        return self.scheduled_class.datetime < timezone.now()

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.scheduled_class.is_full:
                raise ValidationError("This class is fully booked.")
    
        if self.is_past:
            raise ValidationError("Cannot book past classes.")
        
        # Check for overlapping bookings for the same email
        overlapping = Booking.objects.filter(
            email=self.email,
            scheduled_class__datetime=self.scheduled_class.datetime
        ).exclude(pk=self.pk)
        if overlapping.exists():
            raise ValidationError("You already have a booking at this time.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.name} in {self.scheduled_class.title} {(self.scheduled_class.fitness_class.name)} on {self.scheduled_class.datetime.strftime('%Y-%m-%d %H:%M')}"

