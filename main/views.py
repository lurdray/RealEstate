from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import *
from django.contrib import messages

# Create your views here.

def index(request):
	settings = Setting.objects.all()
	properties = Property.objects.all().order_by('-pub_date')[:6]
	headers = Header.objects.all()
	column = Header.objects.all().order_by('?')[:1]

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		subject = request.POST.get('subject')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/')

	context = {"headers":headers,
				"column":column,
				"settings":settings,
				"properties":properties,
			}
	return render(request, "main/index.html", context)


def about(request):
	settings = Setting.objects.all()
	headers = Header.objects.all().order_by('?')[:1]
	column = Header.objects.all().order_by('?')[:1]

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		subject = request.POST.get('subject')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/about')

	context = {"settings":settings,
				"headers":headers,
				"column":column,	
			}
	return render(request, "main/about.html", context)

def properties(request):
	properties = Property.objects.all()
	settings = Setting.objects.all()
	headers = Header.objects.all().order_by('?')[:1]
	column = Header.objects.all().order_by('?')[:1]

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		subject = request.POST.get('subject')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/project')

	context = {"settings":settings,
				"headers":headers,
				"column":column,
				"properties":properties,
			}
	return render(request, "main/project.html", context)

def contact(request):
	settings = Setting.objects.all()
	headers = Header.objects.all().order_by('?')[:1]
	column = Header.objects.all().order_by('?')[:1]



	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		subject = request.POST.get('subject')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject)
		contact_model.save()
		messages.success(request, "Your message has been delivered")
		return HttpResponseRedirect('/contact')

		#response = "We will get back to you shortly!"

	context = {"settings":settings,
				"headers":headers,
				"column":column,
					}
	return render(request, "main/contact.html", context)
