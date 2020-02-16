from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.

class UserInfo(models.Model):
  #linking to user model through one to one relation
  users = models.OneToOneField(User, on_delete=models.CASCADE)

  #additional
  user_type = models.CharField(max_length=6)
  user_amount = models.IntegerField(default=0)

  def __str__(self):
    return self.users.username

class prof(models.Model):
  Name = models.CharField(max_length=100)
  course = models.CharField(max_length=100) #maxlength required
  description = models.TextField(blank=True, null=True)
  salary = models.IntegerField()
  summary = models.TextField()
  Featured = models.BooleanField()

  def __str__(self):
    return self.Name

    





  