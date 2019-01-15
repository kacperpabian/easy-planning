from django.contrib import admin
from school_schedule import models

# Register your models here.
admin.site.register(models.School)
admin.site.register(models.Schedule)
