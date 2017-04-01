import requests
import json 
def sendMessage():
	url="http://api.flock.co//v1/chat.sendMessage"
	d={
				"name":"Orient",
				"profileImage":"http://i.imgur.com/pAKIUxV.jpg"

				}
	payload={
	"to":"g:c38413fd823545f6af4e445452c36d6e",
	"text":"Shivam is out of Bitcap \n thanks and regards",
	"token":"67c8351f-32c7-487b-b6c3-de725daea30c",
	"sendAs":json.dumps(d)
	}
	headers={
	"Content-Type":"application/x-www-form-urlencoded",
	"Content-Length":"70"
	}
	r=requests.post(url,data=payload,headers=headers)
	print r
	print r.text

sendMessage()