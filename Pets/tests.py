from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Pet



class PetTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('pet_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('pet_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Pet/pet-list.html')
        self.assertTemplateUsed(response, 'base.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.Pet = Pet.objects.create(
            name='test',
            owner=1,
            desc="test info",
            color = "test info 2"
        )

    def test_str_method(self):
        self.assertEqual(str(self.Pet),"test")

    def test_detail_view(self):
        url = reverse('pet_detail', args=[self.Pet.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'Pet/pet-detail.html')

    def test_create_view(self):
        obj={
            'name':"test2",
            'owner':5,
            'desc': "info...",
            'color': "info ..."
            
        }

        url = reverse('pet_create')
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Thing.objects.all()),2)
        self.assertRedirects(response, reverse('pet_detail', args=[2]))

