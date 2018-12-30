from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=225)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)
    body=models.TextField()
    url=models.TextField()
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def summary(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date_preety.strftime('%b %e, %Y')

    def __str__(self):
        return self.title
