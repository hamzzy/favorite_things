from rest_framework.test import APIClient, APITestCase
from api.models import Category
from api.serializer import CategorySerializer


class MainViewTest(APITestCase, APIClient):
    client = APIClient()

    @staticmethod
    def create_category(name):
        return Category.objects.create(name=name)

    def setUp(self):
        category = [
            {
                'name': 'reading'
            },

            {
                'name': ' place'
            },

            {
                'name': 'people'
            },

        ]
        for fav in category:
            self.create_category(name=fav['name'])

    def tearDown(self):
        fav = Category.objects.all()
        for f in fav:
            f.delete()

    def test_create_category(self):
        category = {
            'name': 'cycling'
        }

        url = '/api/v1/categories/'
        response = self.client.post(url, data=category)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['msg'], 'category created')

    def test_List_category(self):
        url = '/api/v1/categories/'
        cat = Category.objects.all()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(cat))
