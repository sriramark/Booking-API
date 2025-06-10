from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class FitnessClass(models.Model):
    name = models.CharField(max_length=100, unique=True) # Nmae of the fitness class, ex: "Yoga", "Zumba"
    description = models.TextField()
    instructors = models.ManyToManyField(
        Instructor,
        related_name='fitness_classes', 
        help_text="Instructors who can teach this class"
    )

    def __str__(self):
        return self.name
    
