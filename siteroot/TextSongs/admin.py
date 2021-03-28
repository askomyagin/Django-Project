from django.contrib import admin
from TextSongs import models

admin.site.register(models.Performers)
admin.site.register(models.Albums)
admin.site.register(models.Songs)
admin.site.register(models.OrderText)
# Register your models here.
