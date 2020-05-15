import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question, Survey
from . import views
from .forms import SurveyForm
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class QuestionModelTests(TestCase):
	
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

class TestSurvey(TestCase):

	def test_survey_invalid(self):
		info = {
			'user': 'testing123',
	    	'art': '1', #invalid
	    	'biography': 2.5,
	    	'business': 2.5,
	    	'classics': 2.5,
	    	'crime': 2.5,
	    	'fantasy': 2.5,
	    	'fiction': 2.5,
			'horror': 2.5,
			'humor': 2.5,
			'mystery': 2.5,
			'nonfiction': 2.5,
			'romance': 2.5,
			'suspense': 2.5,
			'sports': 2.5,
			'young_adult': 2.5,
			'average_read_time': '1',
			'last_book': 'Harry Potter',
			'rating':  '4',
			'favorite_author': 'J.K Rowling',
    	}

		form = SurveyForm(info)
		self.assertFalse(form.is_valid())


# FRONTEND TESTING
class TestPolls(TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/register")
		
	def test_survey_valid_form(self):
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

	def test_survey_invalid_form(self):
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
		element11.send_keys("testing12345")

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

		element27 = self.driver.find_element_by_id("id_last_book")
		element27.send_keys("Harry Potter")

		element29 = self.driver.find_element_by_id("id_favorite_author")
		element29.send_keys("J.K Rowling")

		element30 = self.driver.find_element_by_id("sub")
		element30.click()

		self.assertEquals(self.driver.current_url, "http://127.0.0.1:8000/survey/")