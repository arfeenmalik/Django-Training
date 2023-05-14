from django.contrib import admin
from . import models

admin.site.register(models.CatCity)
admin.site.register(models.CatTrainingType)
admin.site.register(models.Resource)
admin.site.register(models.ResourceItem)
admin.site.register(models.Training)
