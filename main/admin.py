from django.contrib import admin
from .models import Banner, Gallery, AboutUs, WhyUs, OurMission, Instructions
from . import models

# COUNTRY / TRIP
admin.site.register(models.Country)
admin.site.register(models.Locations)
admin.site.register(models.LocationImage)
admin.site.register(models.Trip)
admin.site.register(models.TripDays)
admin.site.register(models.Service)
admin.site.register(models.TripImages)
admin.site.register(models.TripOrder)
admin.site.register(models.Blog)


admin.site.register(Banner)
admin.site.register(Gallery)
admin.site.register(AboutUs)
admin.site.register(WhyUs)
admin.site.register(OurMission)
admin.site.register(Instructions)























