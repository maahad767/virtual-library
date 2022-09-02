from django.test import SimpleTestCase

from django.urls import reverse, resolve

from virtual_library.views import (HomeView, LoginView, RegisterView, LogoutView, 
    ProfileView, ProfileUpdateView, ProductCreateView, ProductDetailView, 
    OrderDetailView, OrderCreateView)


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterView)
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, ProfileView)
    
    def test_profile_update_url_is_resolved(self):
        url = reverse('profile_update')
        self.assertEquals(resolve(url).func.view_class, ProfileUpdateView)
    
    def test_product_create_url_is_resolved(self):
        url = reverse('product_create')
        self.assertEquals(resolve(url).func.view_class, ProductCreateView)
    
    def test_product_detail_url_is_resolved(self):
        url = reverse('product_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)

    def test_order_create_url_is_resolved(self):
        url = reverse('order_create', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrderCreateView)

    def test_order_detail_url_is_resolved(self):
        url = reverse('order_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, OrderDetailView)
