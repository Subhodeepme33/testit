from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from msitmcaapp.models import Student
# Create your views here.
def homepage(request):
	return render(request, "index.html")

def secondpage(request):
	return render(request, "second.html")

def saveUser(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		uname = request.POST['uname']
		passwd = request.POST['pass']
		cnf_pass = request.POST['cnf_pass']
		if passwd == cnf_pass:
			user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=passwd)
			user.save()
			print(user)
			return redirect('/second')
		else:
			messages.error(request, 'Failed')
			return redirect('/')
	else:
		return HttpResponse('<script> alert("Submission Error...!!!") </script>')


def login(request):
	if request.method == 'POST':
		username = request.POST['uname']
		password = request.POST['pass']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				request.session.set_expiry(86400)
				auth.login(request, user)
				return redirect('/afterlogin')
			else:
				return HttpResponse('<script> Logged out </script>')
		else:
			messages.error(request, "Wrong Info")
			return('/second')
	else:
		return HttpResponse('<script> alert("Submission Error...!!!") </script>')


def afterlogin(request):
	return render(request, "home.html")

def logout(request):
	auth.logout()
	return redirect('/second')

def fillup(request):
	if request.method == 'POST':
		phone = request.POST['phone']
		address = request.POST['address']
		country = request.POST['country']
		userdata = Student(phone=phone, address=address, country=country)
		userdata.save()
		print(userdata)
		return redirect('/second')
		
	else:
		return HttpResponse('<script> alert("Submission Error...!!!") </script>')


def datadel(request):
	if request.method=='POST':
		email = request.POST['email']

		if User.objects.filter(email=email).exists():
			delt = User.objects.get(email=email)
			delt.delete()
			return redirect('/')

		else:
			return redirect()
	else:
		return render(request, "delete.html")

def updateData(request):
	if request.method=='POST':
		email = request.POST['email']
		name = request.POST['name']

		User.objects.filter(email=email).update(name=name)
		return redirect()
	else:
		return render()

def searchData(request):
	if request.method == 'POST':
		email = request.POST['email']
		if User.objects.filter(email=email).exists():
			data = User.objects.get(email)
			return render(request, "home.html", {'data': data})
		else:
			messages.error(request, "No data found")
			return redirect()
	else:
		return render(request, "something.html")


def forgotpassword(request):
	if request.method == 'POST':
		email = request.POST['email']
		new_p = request.POST['newpass']
		u = User.objects.get(email=email)
		u.set_password(new_p)
		u.save()
		return redirect()
	else:
		return redirect()