from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from orient.models import data , Users  , Saved 

import requests
import json
from django.http import HttpResponse
from orient.models import data , Users  , Saved 
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
		response={
		"text":"Wait a Second"
		}
		response=json.dumps(response,indent=4)
		data2 = json.loads(request.body)

		if data2["name"] == "app.install" :
			print 'hellooooooo'
			print data2['token']
			
			v = Users.objects.get_or_create(user_token = data2["token"])[0]
			v.user_id = data2['userId']
			v.save()
			print 'hellooooooo'
			return HttpResponse('ok')

		elif data2['name'] == 'client.slashCommand' :
			print ' suppppppp'
		
			sendMessage(data2['chat'] , data2['userId'])




		
				


	
	except Exception as e:
		print ecommand

	try:	
		print "received an event"
		print "The request body is ",request.body
		response={
		"text":"Wait a Second"
		}
		response=json.dumps(response,indent=4)
		data2 = json.loads(request.body)
		sender_id = data2["message"]["from"]
		print sender_id
		reciever_id = data2["message"]["to"]
		print reciever_id

		if data2["message"]["text"]  == "hi":
			print 'hellooooooo1234'
			# print data['token']
			
			# v = Users.objects.get_or_create(user_token = data["token"])[0]
			# v.user_id = data['userId']
			# v.save()
			print 'hellooooooo'
			sendMessage2(sender_id , "hi how are you , how can i help you" )

		if data2["message"]["text"].lower()  == "#developer":
			print 'hellooooooo12345'
			# print data['token']
			v = data.objects.all().filter(tags = 'Developer')
			print v
			for i in v:
				print "here are devs"
				print i.first_name
				sendMessage2(sender_id , i.first_name)
			
			# v = Users.objects.get_or_create(user_token = data["token"])[0]
			# v.user_id = data['userId']
			# v.save()
			print 'hellooooooo'
			sendMessage2(sender_id , "here all all the developers for you " )
	
			# return HttpResponse('ok')

		# elif data['name'] == 'client.slashCommand' :
		# 	print ' suppppppp'
		
		# 	sendMessage(data['chat'] , data['userId'])




		
				


	
	except Exception as e:
		print e	
	return HttpResponse(response)



def sendMessage(g_id , u_id ):
	print ' sosososo'
	print g_id
	print u_id
	v = Users.objects.get(user_id = u_id)
	print v 
	print v.user_token
	url="http://api.flock.co//v1/chat.sendMessage"
	
	payload={
	"to":g_id,
	"text":"Shivam is out of Bitcap \n thanks and regards",
	"token":v.user_token,
	# "sendAs":json.dumps(d)
	}
	headers={
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"70"
	}
	r=requests.post(url,data=payload,headers=headers)
	print r
	print r.text

def sendMessage2(u_id , message_text ):
	d={
				"name":"Orient",
				"profileImage":"http://i.imgur.com/pAKIUxV.jpg"

				}

	print ' sosososo'
	# print g_id
	print u_id
	v = Users.objects.get(user_id = u_id)
	# print v 
	# print 
	url="http://api.flock.co/v1/chat.sendMessage"
	
	payload={
	"to":u_id,
	"text":message_text,
	"token": 'ba0af222-e3b0-4686-b2d7-ea9fa7839cc9'
,
	"sendAs":json.dumps(d)
	}
	headers={
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"70"
	}
	r=requests.post(url,data=payload,headers=headers)
	print r
	print r.text

def index(request):
	# payload1 = {'response_type': 'code', 'state': '123456789', 'redirect_uri': 'https://fathomless-depths-13330.herokuapp.com/', 'client_id': '86xgcoikz5tvem' }
	# p = requests.get('https://www.linkedin.com/oauth/v2/authorization', params=payload1)
	# print(p)

	code = request.GET.get('code')
	print code 


	payload = {'grant_type': 'authorization_code', 'code': code , 'redirect_uri': 'https://orient-flock.herokuapp.com/linkedin/', 'client_id': '86xgcoikz5tvem', 'client_secret': 'bMGSpxX8XNEpxocO'}

	r = requests.post('https://www.linkedin.com/oauth/v2/accessToken', params=payload)
	t = json.loads(r.text)
	print t
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





def card(requests):
	q = Users.objects.get(user_id = 'u:mgmjkx1mjww22dx1')

	p = q.data_set.get_or_create()[0]
	context_dict = {}
	context_dict['first_name'] = p.first_name
	context_dict['last_namelast_name'] = p.last_name
	context_dict['headline'] = p.headline
	context_dict['location'] = p.location 
	context_dict['summary'] = p.summary
	context_dict['picture_url'] = p.picture_url
	context_dict['email_address'] = p.email_address
	context_dict['public_profile_url'] = p.public_profile_url
	return render(request,'orient/card.html',context_dict)





