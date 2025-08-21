from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Check out this</h1>")
                

class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_current_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)        

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        # python is case sensistive as you know so if i change to about page is will show an error
        self.assertContains(response, "<h1>About Page</h1>") 
        self.assertEqual(response.status_code, 200)
        
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Check out this")   
        