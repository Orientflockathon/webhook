from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def check(request):
	return HttpResponse("Hey,This worked")
####### Listening for flock events here #############
@csrf_exempt
def listenEvent(request):
	print "received an event"
	print "The request body is ",request.body
	return HttpResponse("recorded event")

