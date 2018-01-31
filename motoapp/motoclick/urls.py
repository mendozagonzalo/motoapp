
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from motoclick import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('api.urls', namespace='api')),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)