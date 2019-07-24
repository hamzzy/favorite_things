from rest_framework.test import APIClient, APITestCase
from api.models import Favorite



class MainViewTest(APITestCase, APIClient):
    client = APIClient()

    @staticmethod
    def create_favorite(user, title='', ranking=0, category=''):
        return Favorite.objects.create(customuser=user, title=title,
                                       metadata="\"{}\"", ranking=ranking,
                                       category=category, description="helping hand")

    def setUp(self):
        favorites = [
            {
                'title': 'reading',
                'ranking': 1,
                'category': 'ppl'
            },

            {
                'title': 'reading',
                'ranking': 5,
                'category': 'pl'
            },

            {
                'title': 'reading',
                'ranking': 3,
                'category': 'fo'
            },

        ]

        for fav in favorites:
            self.create_favorite(title=fav['title'], ranking=fav['ranking'], category=fav['category'])

    def tearDown(self):
        pass
        # fav = Favorite.objects.filter(user=user.id)
        # for f in fav:
        #     f.delete()

