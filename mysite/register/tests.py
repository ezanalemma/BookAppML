from django.test import TestCase
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
# Create your tests here. 

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
