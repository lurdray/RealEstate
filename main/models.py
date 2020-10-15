from django.db import models
from django.utils import timezone



class Header(models.Model):
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=100, default="none")
	description = models.TextField()

	def __str__(self):
		return self.title

class Setting(models.Model):

	STATUS = (
		('True', 'True'),
		('False', 'False'),
	)
	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=350)
	description = models.CharField(max_length=350)
	address = models.CharField(blank=True, max_length=150)
	company = models.CharField(blank=True, max_length=150)
	phone = models.CharField(blank=True, max_length=15)
	fax = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=50)
	footer = models.CharField(blank=True, max_length=50)
	newsletter = models.CharField(blank=True, max_length=50)
	project = models.CharField(blank=True, max_length=50)
	years = models.CharField(blank=True, max_length=50)
	professionals = models.CharField(blank=True, max_length=50)
	machines = models.CharField(blank=True, max_length=50)
	icon = models.ImageField(blank=True, upload_to='images')
	facebook = models.CharField(blank=True, max_length=50)
	instagram = models.CharField(blank=True, max_length=50)
	twitter = models.CharField(blank=True, max_length=50)
	aboutheader = models.TextField(blank=True, max_length=500)
	aboutus = models.TextField(blank=True, max_length=500)
	mission = models.TextField(blank=True, max_length=500)
	vision = models.TextField(blank=True, max_length=500)
	values = models.TextField(blank=True, max_length=500)
	whoweare = models.TextField(blank=True, max_length=500)
	whatwedo = models.TextField(blank=True, max_length=500)
	contact = models.TextField(blank=True, max_length=500)
	references = models.TextField(blank=True,  max_length=500)
	status = models.CharField(max_length=10, choices=STATUS)

	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	subject = models.CharField(max_length=150, default="none")
	message = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name



class Property(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	price = models.IntegerField()
	sqft = models.CharField(max_length=60, default="none")
	location = models.CharField(max_length=60, default="none")
	room = models.IntegerField()
	shower = models.IntegerField()
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class Comment(models.Model):
	image = models.ImageField(upload_to='images')
	comment = models.TextField()
	name = models.CharField(max_length=60, default="none")
	post = models.CharField(max_length=150, default="none")



