from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('information.urls')),
    path('service/', include('services.urls')),
    path('testim/', include('testimony.urls')),
    path('project/', include('projects.urls')),
    path('invoice/', include('invoices.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)