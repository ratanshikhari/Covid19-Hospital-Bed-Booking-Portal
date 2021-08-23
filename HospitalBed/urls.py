from django.contrib import admin
from django.urls import path, include
from LoginPage.views import displayHDetails, logoutuser, userDetails, viewHDetails
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Covid Hospital Bed Booking Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('LoginPage.urls')),
    path('register/', include('LoginPage.urls')),
    path('homepage/', include('HomePage.urls')),
    path('homepageAL/', include('HomePage.urlsAL')),
    path('protectyourself/', include('ProtectYourself.urls')),
    path('protectyourselfAL/', include('ProtectYourself.urlsAL')),
    path('helpus/', include('HelpUs.urls')),
    path('helpusAL/', include('HelpUs.urlsAL')),
    path('hospitaldetails/', displayHDetails),
    path('logout/', logoutuser),
    path('userdetails/', userDetails),
    path('hospitaldetailsview/', viewHDetails),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

