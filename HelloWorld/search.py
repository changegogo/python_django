# -*-coding: utf-8-*-

from django.shortcuts import render_to_response
from django.http import HttpResponse

# 表单
def search_form(request):
	return HttpResponse(request.COOKIES)
	# return render_to_response('search_form.html')

# 接收请求的数据
def search(request):
	request.encoding='utf-8'
	if 'q' in request.GET:
		if request.GET['q'] != "":
			message = '你搜索的内容为：' + request.GET['q']
		else:
			message = '你提交了空表单'
	return HttpResponse(message)