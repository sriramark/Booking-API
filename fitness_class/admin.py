from django.contrib import admin

from .models import FitnessClass, Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    search_fields = ('name', 'email', )

admin.site.register(FitnessClass)

