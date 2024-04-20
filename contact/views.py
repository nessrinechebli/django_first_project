from pprint import pprint
from django.shortcuts import render
from acount.models import CustomerProfile
import smtplib
from contact.models import Contact
from listings.models import Listing

# Create your views here.
def send_email(subject, message, receiver_address):
    # Your email address and password
    sender_address = "meriemmeriem19alg@gmail.com"
    sender_password = "kdza nxxy ywus oyyc"


    # Set up the subject and body of the email
    header = f"\r\nSubject: {subject}"
    body = f"\r\n{message}"

    # Combine the headers and the body
    combined = header + body

    # Send the email!
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_address, sender_password)
    server.sendmail(sender_address, receiver_address, combined)
    print("Email sent!")

def contact(request):
    if request.method == "POST":
      listing=request.POST.get('listing',"")
      name=request.POST.get('name',"")
      email=request.POST.get('email',"")
      message=request.POST.get('message',"")
      customer=request.user.customerprofile
      subject="contact sur "+listing
      print(listing)
      pprint(request.POST)
      send_email(subject="New Listing", message=f"You have a new listing from {name}.\n\n{email}", receiver_address=email)
      listing=Listing.objects.get(id=listing)
      
      contact=Contact(listing=listing,email=email,customer=customer,content=message,subject=subject)
      contact.save()
      pprint(contact)
    context = {
     
    }
    return render(request, 'pages/dashboard.html')
