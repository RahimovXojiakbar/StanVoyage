from django.contrib import admin
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
admin.site.register(models.Social)

admin.site.register(models.Banner)
admin.site.register(models.Gallery)
admin.site.register(models.AboutUs)
admin.site.register(models.WhyUs)
admin.site.register(models.OurMission)
admin.site.register(models.Instructions)

admin.site.register(models.Comment)





















