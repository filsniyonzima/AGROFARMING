from django.contrib import admin
from .models import Farmer, Agronomist, Stock, SeedRequest, FertilizerRequest

admin.site.register(Farmer)

admin.site.register(Agronomist)
admin.site.register(Stock)
admin.site.register(SeedRequest)
admin.site.register(FertilizerRequest)