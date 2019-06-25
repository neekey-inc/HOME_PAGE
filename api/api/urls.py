from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from django.views.generic.base import RedirectView


admin.site.site_title = 'Neekey.inc【管理サイト】' 
admin.site.site_header = 'Neekey.inc【管理サイト】' 
admin.site.index_title = 'ホームページ管理'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
