from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def check(request):
	return HttpResponse("Hey,This worked")
####### Listening for flock events here #############
def listenEvent(request):
	print request.body
	return HttpResponse("recorded event")

