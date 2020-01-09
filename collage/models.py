from django.db import models

# Create your models here.
class Notice(models.Model):
    subject = models.CharField(max_length=40)
    msg = models.TextField()
    crDate = models.DateTimeField(auto_now_add=True)