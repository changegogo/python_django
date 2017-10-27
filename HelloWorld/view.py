from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
	context = {}
	context["hello"] = "代立旺!"
	context["show"] = True
	context["users"] = [{"name": "dailiwang", "age": 17},
						{"name": "gaolijun", "age": 16}]
	return render(request, 'hello.html', context)