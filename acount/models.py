from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    profile_pic = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    search_history=models.TextField() 
    user=models.OneToOneField(User, on_delete=models.CASCADE) #kon ysupprimer profile/cascade=supprimer user
    STATUS_CHOICES = (("GUEST", "GUEST"), ("PREMIUM", "PREMIUM"), ("NORMAL", "NORMAL"))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    preferences = models.TextField(blank=True)#vide
    background=models.TextField()
    
    def __str__(self) -> str:
        return f'{self.user.username}'
    
    
class AgentProfile(models.Model):
    profile_pic = models.ImageField(upload_to="profiles/%Y/%m/%d/")
    bio = models.TextField()
    tel_num=models.IntegerField()
    is_month_seller=models.BooleanField()
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True) #kon ysupprimer profile/cascade=supprimer user
    def __str__(self) -> str:
        return f'{self.user.username}'
    

# class Status(models.TextChoices):
#     GUEST="GUEST"
#     NORMAL="Normal"
#     PREMIUM="PREMIUM"
#  status = models.CharField(max_length=10, choices=status.choices,default=status.GUEST)

