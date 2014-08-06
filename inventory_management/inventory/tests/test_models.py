import unittest

from ..models import *


class ProductModelTestCase(unittest.TestCase):
    def test_default_inventory_count(self):
        """A new product should have 0 as inventory_count by default"""
        # Pretty naive tests. I'm testing django models here!
        # Just to prove a point
        product = Product.objects.create(name="TestProduct")
        self.assertEqual(product.inventory_count, 0)

    # Uncomment to try coverage.py
    # def test_str(self):
    #     product = Product.objects.create(
    #         name="TestProduct", inventory_count=3)
    #
    #     self.assertEqual(str(product), "TestProduct (3 left)")