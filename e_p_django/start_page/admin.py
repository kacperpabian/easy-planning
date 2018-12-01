from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Schedule)
admin.site.register(models.Subject)
admin.site.register(models.Room)
admin.site.register(models.Teacher)
admin.site.register(models.Class)
