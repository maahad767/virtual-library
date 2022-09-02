from django.test import TestCase
from virtual_library.models.category import Category 

from virtual_library.utils.forms import RegisterForm, BookForm


class TestForms(TestCase):
    def test_register_form_valid(self):
        form = RegisterForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password1': 'abs123131sada',
            'password2': 'abs123131sada',
        })

        self.assertTrue(form.is_valid())
    
    def test_book_form_valid(self):
        category = Category.objects.create(name='Fiction')

        form = BookForm({
            'title': 'test',
            'author': 'test',
            'published_date': '2020-01-01',
            'description': 'test',
            'category': category.id,
            'price': 10,
            'rent': 10,
            'status': 'available',
            'available_from': '2020-01-01',
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form = RegisterForm({
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password1': 'abs123131sada',
            'password2': 'abckakasfasfa',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])

    def test_book_form_invalid(self):
        form = BookForm({
            'title': 'test',
            'author': 'test',
            'published_date': '2020-01-01',
            'description': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['category'], ['This field is required.'])
        self.assertEqual(form.errors['price'], ['This field is required.'])
        self.assertEqual(form.errors['rent'], ['This field is required.'])
        self.assertEqual(form.errors['status'], ['This field is required.'])
        self.assertEqual(form.errors['available_from'], ['This field is required.'])

