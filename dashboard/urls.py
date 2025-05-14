from django.urls import path, include

urlpatterns = [
    path('auth/', include('dashboard.auth.urls')),
    path('about/', include('dashboard.AboutWhyUS.urls')),
    path('banner/', include('dashboard.Banner.urls')),
    path('blog/', include('dashboard.Blog.urls')),
    path('comment/', include('dashboard.Comment.urls')),
    path('country/', include('dashboard.Country.urls')),
    path('gallery/', include('dashboard.Gallery.urls')),
    path('instructions/', include('dashboard.Instructions.urls')),
    path('ourmission/', include('dashboard.OurMission.urls')),
    path('social/', include('dashboard.SocialContactInfo.urls')),
    path('testimionals/', include('dashboard.Testimionals.urls')),
    path('traditions/', include('dashboard.Traditions.urls')),
    path('trip/', include('dashboard.Trip.urls'))
]