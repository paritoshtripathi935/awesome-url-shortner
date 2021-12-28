import re
from django.conf.urls import url
from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import HttpResponse
"""
In the Django framework, views are Python functions or classes that receive a web request and return a web response. 
The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page.

"""

# request is sent form urls.py to views.py where web response is genrated 
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)