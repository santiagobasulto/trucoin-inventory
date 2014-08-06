from tastypie import resources
from tastypie.authorization import Authorization

from .models import *
from .validators import TooMuchInventoryValidator

__all__ = ['ProductResource']


class ProductResource(resources.ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        authorization = Authorization()
        validation = TooMuchInventoryValidator()