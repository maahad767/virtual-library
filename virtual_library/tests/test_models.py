from datetime import timedelta, datetime
from django.test import TestCase
from virtual_library.models import User, Category, Book, RentOrder, Rating


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser'
        )
        self.category = Category.objects.create(
            name='testcategory'
        )   
        self.book = Book.objects.create(
            owner=self.user,
            title='testbook',
            author='testauthor',
            published_date='2020-01-01',
            description='testdescription',
            category=self.category,
            price=10,
            rent=10,
            status='available',
        )

    def test_user_model(self):
        user = User.objects.create(
            username='test')

        self.assertEqual(user.username, 'test')
        self.assertEqual(User.objects.count(), 2)

    def test_category_model(self):
        category = Category.objects.create(
            name='test')

        self.assertEqual(category.name, 'test')
    
    def test_book_model(self):
        book = Book.objects.create(
            owner=self.user,
            title='test',
            author='test',
            published_date='2020-01-01',
            description='test',
            category=self.category,
            price=10,
            rent=10,
            status='available',
            available_from='2020-01-01',
        )

        self.assertEqual(book.owner, self.user)
        self.assertEqual(book.title, 'test')
        self.assertEqual(book.author, 'test')
        self.assertEqual(book.published_date, '2020-01-01')
        self.assertEqual(book.description, 'test')
        self.assertEqual(book.category, self.category)
        self.assertEqual(book.price, 10)
        self.assertEqual(book.rent, 10)
        self.assertEqual(book.status, 'available')
        self.assertEqual(book.available_from, '2020-01-01')
    
    def test_rent_order_model(self):
        return_date = timedelta(days=30) + datetime.now().date()
        rent_order = RentOrder.objects.create(
            user=self.user,
            book=self.book,
            return_date=return_date,
        )
        self.assertEqual(RentOrder.objects.count(), 1)
        self.assertEqual(rent_order.user, self.user)
        self.assertEqual(rent_order.book, self.book)
        self.assertEqual(rent_order.return_date, return_date)
    
    def test_rating_model(self):
        rating = Rating.objects.create(
            user=self.user,
            book=self.book,
            rating=5,
        )
        self.assertEqual(rating.user, self.user)
        self.assertEqual(rating.book, self.book)
        self.assertEqual(rating.rating, 5)
    
