from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.ChoiceHorse)
admin.site.register(models.HorseTour)
admin.site.register(models.Comment)
admin.site.register(models.Category)