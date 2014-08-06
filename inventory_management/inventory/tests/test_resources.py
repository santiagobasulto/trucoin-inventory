import json

from django.test import TestCase
from django.test.client import RequestFactory

from tastypie.exceptions import ImmediateHttpResponse

# I like to use factories instead of "fixtures" for versioned APIs because
# underlying models might change, but the interfaces must been kept
from .factories import ProductFactory
from ..resources import ProductResource
from ..models import Product


class ProductResourceTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.product_resource = ProductResource()

    def test_GET_list_return_objects_and_count(self):
        """Should get a list of products with meta data"""
        product = ProductFactory.create()
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 1)

        request = self.factory.get("/api/v1/product/")
        response = self.product_resource.dispatch_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._charset, 'utf-8')

        content = json.loads(response.content.decode(response._charset))

        self.assertTrue('meta' in content)
        self.assertTrue('total_count' in content['meta'])
        self.assertEqual(content['meta']['total_count'], 1)

        self.assertTrue('objects' in content)
        objects = content['objects']
        self.assertEqual(len(objects), 1)
        obj1 = objects[0]
        self.assertEqual(obj1['name'], product.name)

    def test_GET_individual_product(self):
        """Should get an individual product by ID"""
        product = ProductFactory.create()
        ProductFactory.create()

        # Preconditions
        self.assertEqual(Product.objects.all().count(), 2)

        url = "/api/v1/product/{}/".format(product.id)
        request = self.factory.get(url)
        response = self.product_resource.dispatch_detail(
            request, pk=product.id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response._charset, 'utf-8')

        content = json.loads(response.content.decode(response._charset))

        self.assertEqual(content['name'], product.name)
        self.assertEqual(content['id'], product.id)

    def test_POST_a_product(self):
        """Should POST and create an individual product"""
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 0)

        url = "/api/v1/product/"
        request = self.factory.post(url, data=json.dumps({
            'name': 'Test Product',
            'description': 'Test description',
            'inventory_count': 3
        }), content_type="application/json")
        response = self.product_resource.dispatch_list(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.all().count(), 1)

    def test_POST_an_invalid_inventory_product(self):
        """Should reject a product with invalid inventory count"""
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 0)

        url = "/api/v1/product/"
        request = self.factory.post(url, data=json.dumps({
            'name': 'Test Product',
            'description': 'Test description',
            'inventory_count': 1000  # Too much!
        }), content_type="application/json")

        with self.assertRaises(ImmediateHttpResponse):
            self.product_resource.dispatch_list(request)

    def test_DELETE_a_product(self):
        """Should delete a product by ID"""
        product = ProductFactory.create()
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 1)

        request = self.factory.delete("/api/v1/product/{}/".format(product.id))
        response = self.product_resource.dispatch_list(request)

        self.assertEqual(response.status_code, 204)

    def test_update_a_product_inventory_count(self):
        """Should update the inventory count of a product through PATCH"""
        product = ProductFactory.create(inventory_count=3)
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 1)
        self.assertEqual(product.inventory_count, 3)

        url = "/api/v1/product/{}/".format(product.id)
        request = self.factory.patch(url, data=json.dumps({
            'inventory_count': 7
        }), content_type="application/json")
        response = self.product_resource.dispatch_detail(
            request, pk=product.id)

        self.assertEqual(response.status_code, 202)