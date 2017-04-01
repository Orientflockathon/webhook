from django.db import models


# Create your models here.

class Users(models.Model):
    # idn = models.CharField(max_length = 250)
    user_id = models.CharField(max_length = 250)

    def __unicode__(self):
        return self.user_id


class data(models.Model):
    # mac_address = models.CharField(max_length = 250,null=True)
    user_id = models.ForeignKey(Users , null=True)
    idn = models.CharField(max_length = 250)

    first_name = models.CharField(max_length = 100 , null=True)
    last_name = models.CharField(max_length = 1000 , null=True)
    headline= models.CharField(max_length = 1000,null=True)
    location= models.CharField(max_length = 10000, null=True)
    summary= models.CharField(max_length = 1000, null=True)
    tags= models.CharField(max_length = 1000, null=True)
    state = models.IntegerField(max_length = 250, null=True , blank  = True)
    picture_url = models.CharField(max_length = 250, null=True)
    public_profile_url = models.CharField(max_length = 11250, null=True)
    email_address = models.CharField(max_length = 250, null=True)
    
    def __unicode__(self):
        return self.email_address

# class login(models.Model):
#     email = models.EmailField(max_length = 250)
#     password1 = models.CharField(max_length = 25)


#     def __unicode__(self):
#         return self.email

class main(models.Model):
    user_id = models.ForeignKey(Users , null=True)    teamid = models.CharField(max_length = 250, null=True)
    profile = models.CharField(max_length = 250, null=True)
    # teamid = models.CharField(max_length = 250, null=True)





class Saved(models.Model):
    idn = models.ForeignKey(Users)


    saved_id = models.CharField(max_length = 250)
    
    def __unicode__(self):
        return self.saved_id     

     

