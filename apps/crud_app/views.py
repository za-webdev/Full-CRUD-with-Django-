# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

def main(request):

	data={
		'users':User.objects.all()
	}
	return render(request,"crud_app/main.html",data)

def index(request):

	return render(request,"crud_app/index.html")

def create(request):
	check=User.objects.validations(request.POST)
	if type(check) is list:
		for error in check:
			messages.add_message(request,messages.ERROR,error)
		return render(request,'crud_app/index.html')
	else:
		return redirect('/')


def remove(request,user_id):
	# if request.method=='POST':
	User.objects.get(id=user_id).delete()

	return redirect('/',{"users":User.objects.get(id=user_id)})
	# else:
	# 	return render(request, "crud_app/remove.html",{"user":User.objects.get(id=user_id)})

def show (request,user_id):

	return render(request,"crud_app/show.html",{"users":User.objects.get(id=user_id)})

def edit (request,user_id):

	return render(request,"crud_app/edit.html",{"user":User.objects.get(id=user_id)})



def edit_here(request,user_id):
	c=User.objects.get(id=user_id)
	c.first_name =request.POST['first_name']
	c.last_name =request.POST['last_name'] 
	c.email =request.POST['email']
	c.save()


	return render(request,"crud_app/show.html",{"users":User.objects.get(id=user_id)})