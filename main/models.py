from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


########################################################
# Social and Contact
########################################################


# Odilbek start

class Social(BaseModel):
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    gmail = models.EmailField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)

class Contact(BaseModel):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_read = models.BooleanField(default=False)

class CompanyInfo(BaseModel):
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)


########################################################
# About Us and Company Data
########################################################


# Abdulloh start
class Banner(BaseModel):
    image = models.ImageField(upload_to='banners')
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    description_ru = models.TextField(default='')
    description_en = models.TextField(default='')
    description_fr = models.TextField(default='')
    description_de = models.TextField(default='')
    description_es = models.TextField(default='')

    order = models.PositiveIntegerField(default=0)


class SmallBanner(BaseModel):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='small_banners')
    
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    


class AboutUs(BaseModel):
    image = models.ImageField(upload_to='about_us')
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    description_en = models.TextField(default='', blank=True)
    description_ru = models.TextField(default='', blank=True)
    description_fr = models.TextField(default='', blank=True)
    description_de = models.TextField(default='', blank=True)
    description_es = models.TextField(default='', blank=True)


class Gallery(BaseModel):
    image = models.ImageField(upload_to='galleries')
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255, null=True,  blank=True )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']



class WhyUs(BaseModel):
    image = models.ImageField(upload_to='why_us')

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    content_en = models.TextField(null=True, blank=True)
    content_ru = models.TextField(null=True, blank=True)
    content_fr = models.TextField(null=True, blank=True)
    content_de = models.TextField(null=True, blank=True)
    content_es = models.TextField(null=True, blank=True)
   
    
class OurMission(BaseModel):
    image = models.ImageField(upload_to='our_mission')

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    content_en = models.TextField(null=True, blank=True)
    content_ru = models.TextField(null=True, blank=True)
    content_fr = models.TextField(null=True, blank=True)
    content_de = models.TextField(null=True, blank=True)
    content_es = models.TextField(null=True, blank=True)

    order = models.PositiveIntegerField(default=0)


class Instructions(BaseModel):
    image = models.ImageField(upload_to='instructions/')
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    content_en = models.CharField(max_length=255)
    content_ru = models.CharField(max_length=255, null=True, blank=True)
    content_fr = models.CharField(max_length=255, null=True, blank=True)
    content_de = models.CharField(max_length=255, null=True, blank=True)
    content_es = models.CharField(max_length=255, null=True, blank=True)
# Abdullh end


class Blog(BaseModel):
    image = models.ImageField(upload_to='blogs')

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    description_en = models.TextField(default='', blank=True, null=True)
    description_ru = models.TextField(default='', blank=True, null=True)
    description_fr = models.TextField(default='', blank=True, null=True)
    description_de = models.TextField(default='', blank=True, null=True)
    description_es = models.TextField(default='', blank=True, null=True)


class BlogImage(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_image') 
    image = models.ImageField(upload_to='blog_image')

    order = models.PositiveIntegerField(default=0)



class Comment(BaseModel):
    image = models.ImageField(upload_to='comments')
    fullname = models.CharField(max_length=255)
    text = models.TextField(default='')
    order = models.PositiveIntegerField(default=0)



class Traditions(BaseModel):
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255, null=True,  blank=True )

    subtitle_en = models.CharField(max_length=255)
    subtitle_ru = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_fr = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_de = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_es = models.CharField(max_length=255,  null=True, blank=True) 

    content_en = models.TextField()
    content_ru = models.TextField(null=True, blank=True)
    content_fr = models.TextField(null=True, blank=True)
    content_de = models.TextField(null=True, blank=True)
    content_es = models.TextField(null=True, blank=True)

    
class Testimionals(BaseModel):
    author = models.CharField(max_length=255)
    content_en = models.CharField(max_length=255)
    content_ru = models.CharField(max_length=255, null=True, blank=True)
    content_fr = models.CharField(max_length=255, null=True, blank=True)
    content_de = models.CharField(max_length=255, null=True, blank=True)
    content_es = models.CharField(max_length=255, null=True, blank=True)

# Odilbek end

########################################################
# Trip and Tour
########################################################




# Nuriniso start

class Country(BaseModel):
    image = models.ImageField(upload_to='countries', null=True, blank=True)
    
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    description_en = models.TextField(default='')
    description_ru = models.TextField(default='')
    description_fr = models.TextField(default='')
    description_de = models.TextField(default='')
    description_es = models.TextField(default='')

class Locations(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    image = models.ImageField(null=True, blank=True,upload_to='city_image')

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    description_en = models.TextField(default='')
    description_ru = models.TextField(default='')
    description_fr = models.TextField(default='')
    description_de = models.TextField(default='')
    description_es = models.TextField(default='')

class LocationImage(BaseModel):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='location_images/')

class Trip(BaseModel):
    image = models.ImageField(upload_to='trip_image')
    
    locations = models.CharField(max_length=255)

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)


    subtitle_en = models.CharField(max_length=255)
    subtitle_ru = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_fr = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_de = models.CharField(max_length=255,  null=True, blank=True)
    subtitle_es = models.CharField(max_length=255,  null=True, blank=True)


    diapazon = models.CharField(max_length=255,  null=True, blank=True)

    duration = models.PositiveIntegerField(default=0)

    order = models.PositiveIntegerField(default=0)

class TripDays(BaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_day')

    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)

    content_en = models.CharField(max_length=255)
    content_ru = models.CharField(max_length=255, null=True, blank=True)
    content_fr = models.CharField(max_length=255, null=True, blank=True)
    content_de = models.CharField(max_length=255, null=True, blank=True)
    content_es = models.CharField(max_length=255, null=True, blank=True)

    order = models.PositiveIntegerField(default=0)

class Service(BaseModel):
    image = models.ImageField(upload_to='service_images/')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL,null=True,blank=True, related_name='services')
    
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255,  null=True, blank=True)
    title_fr = models.CharField(max_length=255,  null=True, blank=True)
    title_de = models.CharField(max_length=255,  null=True, blank=True)
    title_es = models.CharField(max_length=255,  null=True, blank=True)


    content_en = models.TextField(max_length=255)
    content_fr = models.TextField(max_length=255, null=True, blank=True)
    content_de = models.TextField(max_length=255, null=True, blank=True)
    content_ru = models.TextField(max_length=255, null=True, blank=True)
    content_es = models.TextField(max_length=255, null=True, blank=True)

class TripImages(BaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='trip_images')
    order = models.PositiveIntegerField(default=0)
    
class TripOrder(BaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True, blank=True)
    
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_read = models.BooleanField(default=False)

# Nuriniso end
