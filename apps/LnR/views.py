from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt
import re

# Create your views here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
NAME = re.compile(r'[0,1,2,3,4,5,6,7,8,9]')


def index(request):
	return render (request, "index.html")

def register(request):
	if request.method == 'POST':
		user_tuple2 = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['pw'], request.POST['c_pw'], request.POST['alias'],request.POST['dob'])
		if user_tuple2[0]:
			request.session['id'] = user_tuple2[1].id
			request.session['name'] = user_tuple2[1].first_name + " " + user_tuple2[1].last_name
			return redirect('/success')
		else:
			for i in user_tuple2[1]:
				messages.info( request, user_tuple2[1][i], extra_tags = 'rg')
		 	return redirect('/')

			#make user register again
	
def success(request):
	context = {
		"users" : User.userManager.all()
	}
	return render (request, "logged_in.html", context)

def login(request):

	if request.method == 'POST':
		user_tuple = User.userManager.login(request.POST['elogin'] , request.POST['Lpw'])
		if user_tuple[0]:
			request.session['id'] = user_tuple[1].id
			request.session['name'] = user_tuple[1].first_name + " " + user_tuple[1].last_name
			#change request.session to message later or add request.session to flash message later
			return redirect('/success')
		else:	
			for i in user_tuple[1]:
				messages.info( request, user_tuple[1][i], extra_tags = 'lg')
			return redirect('/')


	

