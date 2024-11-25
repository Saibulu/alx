from django.contrib import admin
from . models import Company, students, Slider, Teams, pricings

# Register your models here.
admin.site.register(Company)

admin.site.register(Slider)

admin.site.register(students)

admin.site.register(Teams)

admin.site.register(pricings)

