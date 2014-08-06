import factory

from ..models import *

__all__ = ['ProductFactory']


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'Test Product {}'.format(n))