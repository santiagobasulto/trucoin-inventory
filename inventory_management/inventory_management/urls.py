from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from inventory import urls as inventory_urls

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(inventory_urls.v1_api.urls)),
)
