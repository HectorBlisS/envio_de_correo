from django.conf.urls import url, include
from django.contrib import admin
from correos import urls as correosUrls


urlpatterns = [
	url(r'^correos/',include(correosUrls, namespace='correos')),
    url(r'^admin/', admin.site.urls),
]
