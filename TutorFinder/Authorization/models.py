from django.db import models
class prof(models.Model):
    title = models.CharField(max_length=120) #maxlength required
    description = models.TextField(blank=True, null=True)
    salary = models.IntegerField()
    summary = models.TextField()
    Featured = models.BooleanField()