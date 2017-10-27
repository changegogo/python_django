# -*-encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

def dealpost(request):
	request.encoding = "utf-8"
	ctx = {}
	if request.POST:
		ctx['name'] = request.POST['name']
		ctx['age'] = request.POST['age']
	return render(request, 'post.html', ctx)