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
from django.views.decorators.clickjacking import xframe_options_exempt

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
		v =Users.objects.get_or_create(user_id = sender_id)[0]
		p = v.data_set.get_or_create()[0]
		

			# print 'hellooooooo1234'
			# # print data['token']
			
			# # v = Users.objects.get_or_create(user_token = data["token"])[0]
			# # v.user_id = data['userId']
			# # v.save()
			# print 'hellooooooo'
			# sendMessage2(sender_id , "hi how are you , how can i help you" )

		if data2["message"]["text"].lower()  == "#developer":
			print 'hellooooooo12345'
			# print data['token']
			v = data.objects.all().filter(headline = 'developer')
			print v
			for i in v:
				print "here are devs"
				print i.first_name
				userid = i.user_id 

				sendMessage3( sender_id , userid )
			
			# v = Users.objects.get_or_create(user_token = data["token"])[0]
			# v.user_id = data['userId']
			# v.save()
			print 'hellooooooo'
			sendMessage2(sender_id , "here are all the developers for you " )


		elif data2["message"]["text"].lower()  == "#setup":
			print 'hellooooooo12345'
			# print data['token']
			
			
			
			# print incomingMessage
			sendMessage2(sender_id , "Do you Agree to answer a few questions reply y or n" )
			p.state =1
			p.save()

		elif data2["message"]["text"].lower()  == "hi":
			print 'hellooooooo12345'
			# print data['token']
			
			
			
			# print incomingMessage
			sendMessage2(sender_id , "hey!Waddup,this is orient bot and i will help you search people in groups according to their job profile send your vCards to people and save people who can be of some interest in future. --you can use the coomands shown below" )
			
			sendAttachmentImage('http://i.imgur.com/lR542bC.jpg' , sender_id)
			sendAttachmentImage('http://i.imgur.com/nyVcvDD.jpg' , sender_id)
			sendAttachmentImage('http://i.imgur.com/0wzMzbb.jpg' , sender_id)

		elif p.state == 1:
			p.state = 2
			p.save()
			sendMessage2(sender_id ,'Please enter your name')

		elif p.state == 2:
			print "sososososo"
			p.first_name = data2["message"]["text"]
			p.state = 3
			p.save()
			sendMessage2(sender_id ,'Can i have a profile headline for eg:developer , designer etc.')
			
		elif p.state == 3:
			p.headline = data2["message"]["text"]
			p.state = 4
			p.save()
			sendMessage2(sender_id ,'Enter the city where you live')
			

		elif p.state == 4:
			p.location = data2["message"]["text"]
			p.state = 5
			p.save()
			sendMessage2(sender_id ,'Provide a short description of your profile')

		elif p.state == 5:
			p.summary = data2["message"]["text"]
			p.state = 6
			p.save()
			sendMessage2(sender_id ,'Can i have Email address')

		elif p.state == 6:
			p.email_address = data2["message"]["text"]
			p.state = 7
			p.save()
			sendMessage2(sender_id ,'please attach a  picture that you want to add and send')


		elif p.state == 7:
			p.picture_url = data2["message"]["attachments"][0]["views"]["image"]["thumbnail"]["src"]

			p.state  = 0
			##handle saving image
			p.save()
			sendMessage2(sender_id ,'thanks your profile is all set.')

		# elif data2["message"]["text"].lower() in "hey,hi,supp".split(','):
			##give user the details to use slash commands
			# return 'enter /setup to register without linkedIn /n enter /'

		elif data2["message"]["text"].lower()  == "#shoutout" :
			p.state = 8
			p.save()

			sendMessage2(sender_id ,'Enter profle and your shoutout in this format developer:your message')

		elif p.state == 8:
			a = data2["message"]["text"]
			array = a.lower().split(':')
			print array[0]
			print array[1]
			v = data.objects.all().filter(headline = array[0])
			for i in v :
				print i.user_id

				sendMessage2(i.user_id ,array[1])
	 


			


		else:
			return 'say Hey , hi , sup to start'


	
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
	idn  = u_id.split(':')[1]
	print v 
	print v.user_token
	print idn
	url="http://api.flock.co/v1/chat.sendMessage"
	
	# widgetdict={ "inline": '<html><body><iframe src="https://orient-flock.herokuapp.com/card/mgmjkx1mjww22dx1" "width": 800 "height": 800 ></body></html>' } 
	
	widgetdict={ "src": 'https://orient-flock.herokuapp.com/card/' + idn  ,'height': 600} 

	viewdict={"widget":widgetdict}
	attachmentarrdict={"title":"attachment title","description":"I-Frame","views":viewdict}
	print (attachmentarrdict)
	payload={
	"to":g_id,
	"token":v.user_token,
	# "sendAs":json.dumps(d) , 
		"attachments" :json.dumps([attachmentarrdict] )
	
	}
	headers={
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"70"
	}
	r=requests.post(url,data=payload,headers=headers)
	print r
	print r.text


def sendMessage3(card_id, u_id ):
	print ' sosososo'
	# print g_id
	print u_id
	v = Users.objects.get(user_id = u_id)
	idn  = str(u_id).split(':')[1]
	print v 
	print v.user_token
	print idn
	url="http://api.flock.co/v1/chat.sendMessage"
	
	# widgetdict={ "inline": '<html><body><iframe src="https://orient-flock.herokuapp.com/card/mgmjkx1mjww22dx1" "width": 800 "height": 800 ></body></html>' } 
	
	widgetdict={ "src": 'https://orient-flock.herokuapp.com/card/' + idn  ,'height': 600} 

	viewdict={"widget":widgetdict}
	attachmentarrdict={"title":"attachment title","description":"I-Frame","views":viewdict}
	print (attachmentarrdict)
	payload={
	"to":card_id,
	"token":'ba0af222-e3b0-4686-b2d7-ea9fa7839cc9',
	# "sendAs":json.dumps(d) , 
		"attachments" :json.dumps([attachmentarrdict] )
	
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

	a = request.GET.get('a')
	print a

	




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

@xframe_options_exempt

def card(requests , id):
	# print id.split(:)[1] 
	q = Users.objects.get(user_id = "u:" + id)

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
	context_dict['description'] = p.summary
	return render(requests,'orient/card.html',context_dict)

@xframe_options_exempt

def frame(requests , id):
	context_dict = {}
	context_dict['url'] = 'https://orient-flock.herokuapp.com/card/' + id
	
	return render(requests,'orient/frame.html',context_dict)

def sendAttachmentImage(url1 , u_id):
	url="http://api.flock.co/v1/chat.sendMessage"
	d={
				"name":"Orient",
				"profileImage":"http://i.imgur.com/pAKIUxV.jpg"

				}
	widgetdict={"original": { "src": url1, "width": 400, "height": 400 }}
	viewdict={"image":widgetdict}
	attachmentarrdict={"title":"","description":"","views":viewdict}
	print (attachmentarrdict)
	payload={
	"to":u_id,
	"token":"ba0af222-e3b0-4686-b2d7-ea9fa7839cc9", 
		"attachments" :json.dumps([attachmentarrdict])
	}
	headers={
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"70"
	}
	r=requests.post(url,data=payload,headers=headers)
	print (r)
	print (r.text)