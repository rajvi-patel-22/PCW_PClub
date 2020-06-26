from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.home,name = 'home'),
path('events',views.events,name = 'events'),
path('aboutus',views.aboutus,name = 'aboutus'),
path('resources',views.resources,name = 'resources'),
path('blog',views.blog,name = 'blog'),
path('addblog',views.addblog,name = 'addblog'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)