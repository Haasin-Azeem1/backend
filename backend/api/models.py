from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id = models.IntegerField()
    number = models.IntegerField()
    email = models.CharField(max_length=200)
    session = models.TextField()
