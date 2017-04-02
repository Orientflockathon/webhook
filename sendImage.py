import requests
import json 

def sendAttachmentImage(url1):
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
	"to":"u:mgmjkx1mjww22dx1",
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

sendAttachmentImage("http://i.imgur.com/lR542bC.jpg")
sendAttachmentImage("http://i.imgur.com/nyVcvDD.jpg")
sendAttachmentImage("http://i.imgur.com/0wzMzbb.jpg")
