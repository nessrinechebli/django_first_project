from django.shortcuts import render
from acount.models import CustomerProfile
import smtplib
# Create your views here.
def send_email(subject, message, receiver_address="yawapen977@acentni.com"):
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
          listing=request.method == "GET"
    context = {
     
    }
    return render(request, 'pages/dashboard.html')
