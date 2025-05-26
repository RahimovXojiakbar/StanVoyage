from rest_framework import serializers
from main import models


class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        exclude = ['is_active']

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        exclude = ['is_active']

class CompanyInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyInfo
        exclude = ['is_active']

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        exclude = ['is_active']

class SmallBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SmallBanner
        exclude = ['is_active']

class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUs
        exclude = ['is_active']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        exclude = ['is_active']

class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WhyUs
        exclude = ['is_active']

class OurMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OurMission
        exclude = ['is_active']

class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructions
        exclude = ['is_active']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        exclude = ['is_active']

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogImage
        exclude = ['is_active']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ['is_active']

class TraditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Traditions
        exclude = ['is_active']

class TestimionalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Testimionals
        exclude = ['is_active']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        exclude = ['is_active']
    
class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Locations
        exclude = ['is_active']

class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationImage
        exclude = ['is_active']

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Trip
        exclude = ['is_active']

class TripDaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TripDays
        exclude = ['is_active']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        exclude = ['is_active']

class TripImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TripImages
        exclude = ['is_active']

class TripOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TripOrder
        exclude = ['is_active']   

