from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import NewUserForm

# Create your views here.
def register(response):
	if response.method == "POST":
		form = NewUserForm(response.POST)
		if form.is_valid():
			user = form.save();
			username = form.cleaned_data.get('username')
			messages.success(response, f"New Account created: {username}")
			login(response, user)
			messages.info(response, f"You are now logged in as {username}")
			return redirect("/home")
		else:
			for msg in form.error_messages:
				messages.error(response, f"{msg}: {form.error_messages[msg]}")



	form = NewUserForm()
	return render(response, "register/register.html", {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/register")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "register/login.html",
                    context={"form":form})