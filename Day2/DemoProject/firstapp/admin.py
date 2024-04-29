from django.contrib import admin
from .models import Person
from . import models
# Register your models here.
# admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','age', 'created_date', 'last_updated')

admin.site.register(models.Person, PersonAdmin)