from datetime import timedelta, datetime
from time import timezone
from django.test import TestCase, Client
from django.urls import reverse

from virtual_library.models import User, Category, Book, Rating, RentOrder


class TestViews(TestCase):
    
        def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user(username='test')
            self.user.set_password('test')
            self.user.save()
            self.client.force_login(self.user)
            self.category = Category.objects.create(name='test')
            self.book = Book.objects.create(title='test', author='test', published_date='2020-01-01', description='test', owner=self.user, category=self.category, price=10, rent=10, status='available', available_from='2020-01-01')
            self.rating = Rating.objects.create(book=self.book, user=self.user, rating=5)
            self.order = RentOrder.objects.create(book=self.book, user=self.user, return_date='2020-01-01')
    
        def test_order_detail_view(self):
            response = self.client.get(reverse('order_detail', args=[self.order.pk]))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'order.html')
            self.assertContains(response, self.order.book.title)
            self.assertContains(response, self.order.user.username)
        
        def test_order_create_view_post(self):
            self.client.force_login(self.user)
            return_date = timedelta(days=30) + datetime.now()
            book = Book.objects.create(title='test', author='test', published_date='2020-01-01',
                    description='test', owner=self.user, category=self.category, price=12, rent=12,
                    status='available')
            response = self.client.get(reverse('order_create', args=[book.pk]))
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('order_detail', args=[2]))
            self.assertEqual(RentOrder.objects.count(), 2)
            updated_book = Book.objects.get(id=book.pk)
            self.assertEqual(updated_book.status, 'on_rent')
            self.assertEqual(updated_book.available_from, return_date.date())

        def test_create_product_view_post(self):
            self.client.force_login(self.user)
            response = self.client.post(reverse('product_create'), {
                'title': 'test',
                'author': 'test',
                'published_date': '2020-01-01',
                'description': 'test',
                'category': self.category.pk,
                'price': 10,
                'rent': 10,
                'status': 'available',
                'available_from': '2020-01-01'
            })
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('product_detail', args=[2]))
            self.assertEqual(Book.objects.count(), 2)
            self.assertEqual(Book.objects.get(id=2).title, 'test')

        def test_product_detail_view(self):
            response = self.client.get(reverse('product_detail', args=[self.book.pk]))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'product_detail.html')
            self.assertContains(response, self.book.title)
            self.assertContains(response, self.book.author)
            self.assertContains(response, self.book.owner.first_name)
            self.assertContains(response, self.book.category.name)
            self.assertContains(response, self.book.price)
            self.assertContains(response, self.book.rent)
        
        def test_profile_view(self):
            response = self.client.get(reverse('profile'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'profile.html')
            self.assertContains(response, self.user.username)
            self.assertContains(response, self.user.email)
            self.assertContains(response, self.user.first_name)
            self.assertContains(response, self.user.last_name)
            self.assertContains(response, self.user.phone)
            self.assertContains(response, self.user.address)
        

        def test_profile_update_view_post(self):
            self.client.force_login(self.user)
            response = self.client.post(reverse('profile_update'), {
                'email': 'new_email@gmail.com',
                'first_name': 'new first name',
                'last_name': 'new last name',
                'phone': '123456789',
                'address': 'new address'
            })
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('profile'))
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(User.objects.get(id=1).email, 'new_email@gmail.com')
            self.assertEqual(User.objects.get(id=1).phone, '123456789')
            self.assertEqual(User.objects.get(id=1).first_name, 'new first name')
            self.assertEqual(User.objects.get(id=1).last_name, 'new last name')
            self.assertEqual(User.objects.get(id=1).address, 'new address')

