from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from instadealz.models import Product


# Create your tests here.
class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_product = Product.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_product.save()

    def test_product_model(self):
            product = Product.objects.get(id=1)
            actual_owner = str(product.owner)
            actual_name = str(product.name)
            actual_description = str(product.description)
            self.assertEqual(actual_owner,'testuser')
            self.assertEqual(actual_name, 'rake')
            self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
            
    def test_list_page_status_code(self):
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status_code(self):
        url = reverse("product_detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



