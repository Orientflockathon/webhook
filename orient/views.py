from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def check(request):
	return HttpResponse("Hey,This worked")
####### Listening for flock events here #############
def listenEvent(request):
	try:	
		print "received an event"
		print "The request body is ",request.body

	except Exception as e:
		print e
	return HttpResponse("recorded event")

