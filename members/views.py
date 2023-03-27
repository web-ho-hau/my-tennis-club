from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

import datetime

def testing(request):

	''' data = [
		{
			'id': 1,
			'firstname': 'John',
			'lastname': 'Doe',
			'age': 22,
			'joined_date': datetime.date(2023, 3, 25)
		},
		{
			'id': 2,
			'firstname': 'Anna',
			'lastname': 'Doe',
			'age': 19,
			'joined_date': datetime.date(2023, 3, 23)
		},
		{
			'id': 3,
			'firstname': 'James',
			'lastname': 'Refsnes',
			'age': 21,
			'joined_date': datetime.date(2023, 3, 19)
		}
	] '''

	template = loader.get_template('template.html')
	# context = {
	# 	'members': data
	# }
	return HttpResponse(template.render({}, request))
	

def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
	context = {
		'mymembers': mymembers
	}
	return HttpResponse(template.render(context, request))


def details(request, id):
	mymember = Member.objects.get(id=id)
	template = loader.get_template('details.html')
	context = {'mymember': mymember}
	return HttpResponse(template.render(context, request))


def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render({}, request))