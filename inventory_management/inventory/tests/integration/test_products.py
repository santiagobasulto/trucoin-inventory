from . import IntegrationTestCase

from ..factories import ProductFactory
from ...models import Product


class ProductResourceIntegrationTestCase(IntegrationTestCase):
    def test_GET_list_return_objects_and_count(self):
        """Should get a list of products with meta data"""
        product = ProductFactory.create()
        # Preconditions
        self.assertEqual(Product.objects.all().count(), 1)

        response = self.app.get(
            '/api/v1/product/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        content = response.json
        self.assertTrue('meta' in content)
        self.assertTrue('total_count' in content['meta'])
        self.assertEqual(content['meta']['total_count'], 1)

        self.assertTrue('objects' in content)
        objects = content['objects']
        self.assertEqual(len(objects), 1)
        obj1 = objects[0]
        self.assertEqual(obj1['name'], product.name)

    # More to come
