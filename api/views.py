from rest_framework.decorators import api_view
from rest_framework.response import Response
from main import models
from . import serializers


@api_view(['GET'])
def social(request):
    social = models.Social.objects.filter(is_active=True)
    serializer = serializers.SocialSerializers(social, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def contact(request):
    serializer = serializers.ContactSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def companyInfo(request):
    company_info = models.CompanyInfo.objects.filter(is_active=True)
    serializer = serializers.CompanyInfoSerializers(company_info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def banner(request):
    banner = models.Banner.objects.filter(is_active=True)
    serializer = serializers.BannerSerializers(banner, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bannerDetail(request, uuid):
    banner = models.Banner.objects.get(uuid=uuid)
    small_banner = models.SmallBanner.objects.filter(is_active=True, banner=banner)

    context =  {
        "banner":serializers.BannerSerializers(banner).data,
        "small_banner":serializers.SmallBannerSerializers(small_banner, many=True).data
    }
    return Response(context)

@api_view(['GET'])
def aboutUs(request):
    about_us = models.AboutUs.objects.filter(is_active=True)
    serializer = serializers.AboutUsSerializers(about_us, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def whyUs(request):
    why_us = models.WhyUs.objects.filter(is_active=True)
    serializer = serializers.WhyUsSerializer(why_us, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ourMission(request):
    our_mission = models.OurMission.objects.filter(is_active=True)
    serializer = serializers.OurMissionSerializer(our_mission, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def instructions(request):
    instructions = models.Instructions.objects.filter(is_active=True)
    serializer = serializers.InstructionsSerializer(instructions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog(request):
    blog = models.Blog.objects.filter(is_active=True)
    serializer = serializers.BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, uuid):
    blog = models.Blog.objects.get(is_active=True, uuid=uuid)
    blog_image = models.BlogImage.objects.filter(is_active=True, blog=blog)

    context = {
        "blog":serializers.BlogSerializer(blog).data,
        "blog_image":serializers.BlogImageSerializer(blog_image, many=True).data
    }
    return Response(context)

@api_view(['GET'])
def comment(request):
    comment = models.Comment.objects.filter(is_active=True)
    serializer = serializers.CommentSerializer(comment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def traditions(request):
    traditions = models.Traditions.objects.filter(is_active=True)
    serializer = serializers.TraditionsSerializer(traditions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def testimionals(request):
    testimionals = models.Testimionals.objects.filter(is_active=True)
    serializer = serializers.TestimionalsSerializer(testimionals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def country(request):
    country = models.Country.objects.filter(is_active=True)
    serializer = serializers.CountrySerializer(country, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def countryDetail(request, uuid):
    country = models.Country.objects.get(is_active=True, uuid=uuid)
    locations = models.Locations.objects.filter(is_active=True, country=country)

    context = {
        "country":serializers.CountrySerializer(country).data,
        "locations":serializers.LocationsSerializer(locations, many=True).data
    }
    return Response(context)

@api_view(['GET'])
def locationDetail(request, uuid):
    location = models.Locations.objects.get(is_active=True, uuid=uuid)
    location_image = models.LocationImage.objects.filter(is_active=True)

    context = {
        "location":serializers.LocationsSerializer(location).data,
        "location_image":serializers.LocationImageSerializer(location_image, many=True).data
    }

    return Response(context)

@api_view(['GET'])
def trip(request):
    trip = models.Trip.objects.filter(is_active=True)
    serializer = serializers.TripSerializer(trip, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tripDetail(request, uuid):
    trip = models.Trip.objects.get(uuid=uuid)
    trip_days = models.TripDays.objects.filter(is_active=True, trip=trip)
    trip_images = models.TripImages.objects.filter(is_active=True, trip=trip)
    services = models.Service.objects.filter(is_active=True, trip=trip)
    trip_order = models.TripOrder.objects.filter(is_active=True, trip=trip)

    context = {
        "trip":serializers.TripSerializer(trip).data,
        "trip_days":serializers.TripDaysSerializer(trip_days, many=True).data,
        "trip_images":serializers.TripImagesSerializer(trip_images, many=True).data,
        "services":serializers.ServiceSerializer(services, many=True).data,
        "trip_order":serializers.TripOrderSerializer(trip_order, many=True).data
    }
    return Response(context)

