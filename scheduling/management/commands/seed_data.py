from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from fitness_class.models import Instructor, FitnessClass
from scheduling.models import ScheduledClass, Booking

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        instructor1, _ = Instructor.objects.get_or_create(name="Alice Johnson", email="alice@example.com", bio="Certified Yoga and Zumba Instructor.")
        instructor2, _ = Instructor.objects.get_or_create(name="Bob Smith", email="bob@example.com", bio="HIIT expert with 5 years of experience.")
        print("Instructors created or retrieved successfully.")
        yoga, _ = FitnessClass.objects.get_or_create(
            name="Yoga",
            defaults={"description": "Relaxing and stretching exercises."}
        )

        zumba, _ = FitnessClass.objects.get_or_create(
            name="Zumba",
            defaults={"description": "Dance-based fitness program."}
        )

        hiit, _ = FitnessClass.objects.get_or_create(
            name="HIIT",
            defaults={"description": "High-intensity interval training."}
        )

        print("Fitness classes created or retrieved successfully.")
        yoga.instructors.add(instructor1)
        zumba.instructors.add(instructor1)
        hiit.instructors.add(instructor2)

        sc1, _ = ScheduledClass.objects.get_or_create(
            fitness_class=yoga,
            title="Morning Yoga Session",
            instructor=instructor1,
            datetime=timezone.now() + timedelta(days=1, hours=11),
            defaults={"total_available_slots": 10}
        )

        sc2, _ = ScheduledClass.objects.get_or_create(
            fitness_class=zumba,
            title="Evening Zumba Blast",
            instructor=instructor1,
            datetime=timezone.now() + timedelta(days=2, hours=20),
            defaults={"total_available_slots": 15}
        )

        sc3, _ = ScheduledClass.objects.get_or_create(
            fitness_class=hiit,
            title="HIIT Power Hour",
            instructor=instructor2,
            datetime=timezone.now() + timedelta(days=3, hours=24),
            defaults={"total_available_slots": 8}
        )

        Booking.objects.get_or_create(scheduled_class=sc1, name="Charlie Patel", email="charlie@example.com")
        Booking.objects.get_or_create(scheduled_class=sc1, name="Dana Lee", email="dana@example.com")

        self.stdout.write(self.style.SUCCESS("✅ Seed data loaded successfully."))

