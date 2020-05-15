import datetime

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import UserBook
from . import views
from selenium import webdriver
from register.views import register
from polls.models import Book
from selenium.webdriver.support.ui import Select

class TestBookThere(TestCase):

	def test_user_book_in_db(self):	
		self.factory = RequestFactory()
		self.user = User.objects.create_user(
            username='testclient', email='testclient@testclient.com', password='thisisatest')
		# create book in DB for testing purposes
		Book.objects.create(
			book_id=1, 
			good_reads_id=1, 
			title="Test", 
			authors='Test', 
			year=1234, 
			genre='fiction', 
			tag_id=1,
			image_url='www.google.com',
			small_image_url='www.google.com',
			isbn=12345678,
			isbn13=12345668,
		)
		request = self.factory.get('/index')
		request.user = self.user
		response = views.index(request)
		self.assertEqual(UserBook.objects.count(), 1)

# FRONTEND TESTING
class TestHomePage(TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/register")

	def test_home_has_book(self):
		element1 = self.driver.find_element_by_id("id_username")
		element1.send_keys("testing1234")

		element2 = self.driver.find_element_by_id("id_email")
		element2.send_keys("testing1@testing.com")
	
		element3 = self.driver.find_element_by_id("id_library_card_number")
		element3.send_keys("123456789")

		element4 = self.driver.find_element_by_id("id_address_line_1")
		element4.send_keys("1234 Hello St")

		element5 = self.driver.find_element_by_id("id_city")
		element5.send_keys("Hayward")

		element6 = self.driver.find_element_by_id("id_state")
		element6.send_keys("CA")

		element7 = self.driver.find_element_by_id("id_postal_code")
		element7.send_keys("123456")

		element8 = self.driver.find_element_by_id("id_password1")
		element8.send_keys("selenium1")

		element9 = self.driver.find_element_by_id("id_password2")
		element9.send_keys("selenium1")

		element10 = self.driver.find_element_by_id("btn")
		element10.click()
	
		element11 = self.driver.find_element_by_id("id_user")
		element11.send_keys("testing1234")

		element12 = self.driver.find_element_by_id("id_art")
		element12.send_keys("1")

		element13 = self.driver.find_element_by_id("id_bio")
		element13.send_keys("1")

		element14 = self.driver.find_element_by_id("id_business")
		element14.send_keys("1")

		element15 = self.driver.find_element_by_id("id_classics")
		element15.send_keys("1")

		element16 = self.driver.find_element_by_id("id_crime")
		element16.send_keys("1")

		element17 = self.driver.find_element_by_id("id_fantasy")
		element17.send_keys("1")

		element18 = self.driver.find_element_by_id("id_fiction")
		element18.send_keys("1")
		
		element19 = self.driver.find_element_by_id("id_horror")
		element19.send_keys("1")

		element = self.driver.find_element_by_id("id_humor")
		element.send_keys("1")

		element20 = self.driver.find_element_by_id("id_mystery")
		element20.send_keys("1")
		
		element21 = self.driver.find_element_by_id("id_nonfiction")
		element21.send_keys("1")

		element22 = self.driver.find_element_by_id("id_romance")
		element22.send_keys("1")

		element23 = self.driver.find_element_by_id("id_suspense")
		element23.send_keys("1")

		element24 = self.driver.find_element_by_id("id_sports")
		element24.send_keys("1")

		element25 = self.driver.find_element_by_id("id_young_adult")
		element25.send_keys("1")

		# element26 = self.driver.find_element_by_id("id_average_read_time")
		element26 = Select(self.driver.find_element_by_id('id_average_read_time'))
		element26.select_by_visible_text('Every Day')
		element26.select_by_value('1')

		element27 = self.driver.find_element_by_id("id_last_book")
		element27.send_keys("Harry Potter")

		element28 = Select(self.driver.find_element_by_id('id_rating'))
		element28.select_by_visible_text('1 Star')
		element28.select_by_value('1')
		

		element29 = self.driver.find_element_by_id("id_favorite_author")
		element29.send_keys("J.K Rowling")

		element30 = self.driver.find_element_by_id("sub")
		element30.click()

		self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/home/")
		elem = self.driver.find_elements_by_id("image")
		self.assertTrue(len(elem) > 0)

	def test_home_click_new_book(self):
		element1 = self.driver.find_element_by_id("id_username")
		element1.send_keys("testing12345")

		element2 = self.driver.find_element_by_id("id_email")
		element2.send_keys("testing1@testing.com")
	
		element3 = self.driver.find_element_by_id("id_library_card_number")
		element3.send_keys("123456789")

		element4 = self.driver.find_element_by_id("id_address_line_1")
		element4.send_keys("1234 Hello St")

		element5 = self.driver.find_element_by_id("id_city")
		element5.send_keys("Hayward")

		element6 = self.driver.find_element_by_id("id_state")
		element6.send_keys("CA")

		element7 = self.driver.find_element_by_id("id_postal_code")
		element7.send_keys("123456")

		element8 = self.driver.find_element_by_id("id_password1")
		element8.send_keys("selenium1")

		element9 = self.driver.find_element_by_id("id_password2")
		element9.send_keys("selenium1")

		element10 = self.driver.find_element_by_id("btn")
		element10.click()
	
		element11 = self.driver.find_element_by_id("id_user")
		element11.send_keys("testing1234")

		element12 = self.driver.find_element_by_id("id_art")
		element12.send_keys("1")

		element13 = self.driver.find_element_by_id("id_bio")
		element13.send_keys("1")

		element14 = self.driver.find_element_by_id("id_business")
		element14.send_keys("1")

		element15 = self.driver.find_element_by_id("id_classics")
		element15.send_keys("1")

		element16 = self.driver.find_element_by_id("id_crime")
		element16.send_keys("1")

		element17 = self.driver.find_element_by_id("id_fantasy")
		element17.send_keys("1")

		element18 = self.driver.find_element_by_id("id_fiction")
		element18.send_keys("1")
		
		element19 = self.driver.find_element_by_id("id_horror")
		element19.send_keys("1")

		element = self.driver.find_element_by_id("id_humor")
		element.send_keys("1")

		element20 = self.driver.find_element_by_id("id_mystery")
		element20.send_keys("1")
		
		element21 = self.driver.find_element_by_id("id_nonfiction")
		element21.send_keys("1")

		element22 = self.driver.find_element_by_id("id_romance")
		element22.send_keys("1")

		element23 = self.driver.find_element_by_id("id_suspense")
		element23.send_keys("1")

		element24 = self.driver.find_element_by_id("id_sports")
		element24.send_keys("1")

		element25 = self.driver.find_element_by_id("id_young_adult")
		element25.send_keys("1")

		# element26 = self.driver.find_element_by_id("id_average_read_time")
		element26 = Select(self.driver.find_element_by_id('id_average_read_time'))
		element26.select_by_visible_text('Every Day')
		element26.select_by_value('1')

		element27 = self.driver.find_element_by_id("id_last_book")
		element27.send_keys("Harry Potter")

		element28 = Select(self.driver.find_element_by_id('id_rating'))
		element28.select_by_visible_text('1 Star')
		element28.select_by_value('1')
		

		element29 = self.driver.find_element_by_id("id_favorite_author")
		element29.send_keys("J.K Rowling")

		element30 = self.driver.find_element_by_id("sub")
		element30.click()

		self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/home/")
		elem = self.driver.find_element_by_id('btn')
		elem.click()
		elem1 = self.driver.find_elements_by_id("image")
		self.assertTrue(len(elem1) > 0)
