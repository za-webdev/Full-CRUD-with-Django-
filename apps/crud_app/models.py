# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def validations(self, post_data):
		errors=[]
		#for first name
		if len(post_data['first_name'])<1:
			errors.append(' First name is required')
		elif len(post_data['first_name'])<3:
			errors.append('Name must be greater than 5 characters or more')
		#for last name
		if len(post_data['last_name'])<1:
			errors.append(' Last name is required')
		elif len(post_data['first_name'])<3:
			errors.append('Name must be greater than 5 characters or more')
		#for email

		if len(post_data['email'])<1:
			errors.append('email is required')
		# elif len(post_data['email'])<15:
		# 	errors.append('email must br greater than 5 characters or more')

		if len(errors)>0:
			return errors

		else:
			return User.objects.create(first_name=post_data['first_name'],last_name=post_data['last_name'],email=post_data['email'])




class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=UserManager()

	def __repr__(self):
		return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)

