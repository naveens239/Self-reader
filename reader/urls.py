from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from pacereader import views

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^read/', views.read, name='read'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

#not to be used if debug is true
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)