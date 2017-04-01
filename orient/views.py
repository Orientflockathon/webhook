from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import requests
import json
from django.http import HttpResponse
from api.models import data , Users , login , Saved 
from django.shortcuts import redirect


access_token = 'AQWaKPLlQEPw-T3-sUakDt6XMpLMU1iuDpz9jzKKySirZxoOEmSwnR_CHPePahHU3eSJ7m5qx2V55jYGe99F5fUs4gjR-1P__bzn0v6Y04YC9ZVMtwMbhCzc7GzZ2Gywmy5NNKGXXsfV_BhGiiTncLTFOXJQrCvEZfiiRATfepeHZbfUWX0'
def check(request):
	return HttpResponse("Hey,This worked")
####### Listening for flock events here #############
@csrf_exempt
def listenEvent(request):
	try:	
		print "received an event"
		print "The request body is ",request.body

	except Exception as e:
		print e
	return HttpResponse("recorded event")

def index(request):
	# payload1 = {'response_type': 'code', 'state': '123456789', 'redirect_uri': 'https://fathomless-depths-13330.herokuapp.com/', 'client_id': '86xgcoikz5tvem' }
	# p = requests.get('https://www.linkedin.com/oauth/v2/authorization', params=payload1)
	# print(p)
	


	




	code = request.GET.get('code')
	print code 

	




	payload = {'grant_type': 'authorization_code', 'code': code , 'redirect_uri': 'https://orient-flock.herokuapp.com/', 'client_id': '86xgcoikz5tvem', 'client_secret': 'bMGSpxX8XNEpxocO'}

	r = requests.post('https://www.linkedin.com/oauth/v2/accessToken', params=payload)
	t = json.loads(r.text)
	z = t['access_token']
	print "hihihihi" + z
	x = requests.get('https://api.linkedin.com/v1/people/~:(id,first-name,email-address,last-name,headline,picture-url,public-profile-url,location,summary,specialties,positions)?format=json', 
                    headers={"Authorization": "Bearer " + z
                     },
                  )
	q = json.loads(x.text)
	idn = q['id']
	v = Users.objects.get_or_create(idn = idn)[0]
	v.idn = idn
	pk = v.pk
	v.save()

	u = v.data_set.get_or_create()[0]
	#u.idm = v
	u.first_name = q['firstName'] 
	u.last_name = q['lastName'] 
	u.headline = q['headline'] 
	u.location = q['location'] 
	try:

		u.summary = q['summary'] 

	except:
		u.summary = "NULL"
	
	try:

		u.tags = q['specialties'] 

	except:
		u.tags = "NULL"
				
	

	try:


		u.picture_url = q['pictureUrl'] 

	except:
		u.picture_url = "NULL"
		

	u.public_profile_url = q['publicProfileUrl'] 
	u.email_address = q['emailAddress'] 
	u.positions = q['positions']
	u.save()





	responseobj = json.dumps(q, indent = 4)






	return HttpResponse(responseobj,content_type = "application/json")
