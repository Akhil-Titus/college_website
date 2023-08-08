from django.contrib import admin

# Register your models here.
from .models import City, Country, Person

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Person)