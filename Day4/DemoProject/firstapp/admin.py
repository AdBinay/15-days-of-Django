from django.contrib import admin
from .models import Person
from . import models
# Register your models here.
# admin.site.register(Person)

class ProfileInline(admin.StackedInline):
    model = models.Profile

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','age', 'created_date', 'last_updated')

    inlines = [
        ProfileInline
    ]


admin.site.register(models.Person, PersonAdmin)

admin.site.register(models.Profile)