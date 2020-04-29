from django.test import TestCase
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django_webtest import WebTest
from selenium import webdriver

class New_User_Form_Test(TestCase):

    # Valid Form Data
    def test_NewUserForm_valid(self):
    	info = {
    		'username': 'testclient',
    		'email': 'user@user.com',
    		'library_card_number': 123456789,
    		'password1': 'test123456',
    		'password2': 'test123456',
    	}
    	form = NewUserForm(info)
    	self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_NewUserForm_invalid(self):
    	info = {
    		'username': 'testclient',
    		'email': 'user',
    		'library_card_number': 1234242342,
    		'password1': 'test',
    		'password2': 'test',
    	}
    	form = NewUserForm(info)
    	self.assertFalse(form.is_valid())


class Login_Test(TestCase):
	def test_Login_valid(self):
		credentials = {
			'username': 'testclient',
    		'email': 'user@user.com',
    		'library_card_number': 123456789,
    		'password1': 'test123456',
    		'password2': 'test123456',
		}
		form = NewUserForm(credentials)
		response = self.client.post('/login/', credentials, follow=True)
		self.assertTrue(form.save().is_authenticated)
		self.assertIsNotNone(form.save())

	def test_Login_invalid(self):
		user = authenticate(username='temporary', password='temporary')
		self.assertIsNone(user)

# FRONTEND TESTING
class TestSignup(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup(self):
        self.driver.get("http://127.0.0.1:8000/register")
        element1 = self.driver.find_element_by_id("id_username")
        element1.send_keys("testing123")

        element2 = self.driver.find_element_by_id("id_email")
        element2.send_keys("testing@testing.com")

        element3 = self.driver.find_element_by_id("id_library_card_number")
        element3.send_keys("123456789")

        element4 = self.driver.find_element_by_id("id_password1")
        element4.send_keys("selenium")

        element5 = self.driver.find_element_by_id("id_password2")
        element5.send_keys("selenium")

        element6 = self.driver.find_element_by_id("btn")
        element6.click()

        self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/home/")
        element7 = self.driver.find_element_by_id("user")
        self.assertEquals(element7.text, "testing123")

    def test_invalid_signup(self):
        self.driver.get("http://127.0.0.1:8000/register")
        element1 = self.driver.find_element_by_id("id_username")
        element1.send_keys("testing123")

        element2 = self.driver.find_element_by_id("id_email")
        element2.send_keys("testing@testing.com")

        element3 = self.driver.find_element_by_id("id_library_card_number")
        element3.send_keys("123456789")

        element4 = self.driver.find_element_by_id("id_password1")
        element4.send_keys("selenium123")

        element5 = self.driver.find_element_by_id("id_password2")
        element5.send_keys("selenium")

        element6 = self.driver.find_element_by_id("btn")
        element6.click()

        self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/register/")
        src = self.driver.page_source
        self.assertTrue('password_mismatch' in src)

    def test_login_logout(self):
        self.driver.get("http://127.0.0.1:8000/register")
        element = self.driver.find_element_by_id("have_login")
        element.click()
        self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/login")
        element1 = self.driver.find_element_by_id("id_username")
        element1.send_keys("testing123")
        element4 = self.driver.find_element_by_id("id_password")
        element4.send_keys("selenium")
        element6 = self.driver.find_element_by_id("log")
        element6.click()
        self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/home/")
        element7 = self.driver.find_element_by_id("user")
        self.assertEquals(element7.text, "testing123")
        element = self.driver.find_element_by_id("logout")
        element.click()
        self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/register")
        

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()


