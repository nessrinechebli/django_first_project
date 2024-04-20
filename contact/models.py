from django.db import models
from acount.models import *
from listings.models import *

class Contact(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.SET_NULL,null=True)
    customer=models.ForeignKey(CustomerProfile,on_delete=models.SET_NULL,null=True)
    contact_date=models.DateField(auto_now_add=True)
    subject=models.CharField(max_length=100)
    content=models.TextField()
    is_viewed=models.BooleanField(default=False)