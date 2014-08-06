from django.conf.urls import patterns, url, include

from tastypie.api import Api

from .resources import ProductResource

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())