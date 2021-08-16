from django.db import models

class userTable(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

class userSession(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_key=models.CharField(max_length=50)

class usergr(models.Model):
    username = models.ForeignKey(userTable, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=50)
    item_quan=models.IntegerField(max_length=3)
    item_status=models.CharField(max_length=50)
    item_date=models.DateField()


