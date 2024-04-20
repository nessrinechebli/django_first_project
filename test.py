# import smtplib

# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#     # smtp.connect('smtp.gmail.com', 465)
#     smtp.login("meriemeriem19alg@gmail.com", "kdza nxxy ywus oyyc")
#     smtp.sendmail(
#         "meriemeriem19alg@gmail.com",
#         "pabac61911@etopys.com",
#         "Subject: So long...\n\nhello world, \n",
#     )


# mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# mail_server.login("meriemeriem19alg@gmail.com", "password")
# mail_server.sendmail(
#     "meriemeriem19alg@gmail.com",
#     "pabac61911@etopys.com",
#     "Subject: So long...\n\nhello world, \n",
# )
# print("the message was send ")
import smtplib


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
send_email("hello","email of meriem","pabac61911@etopys.com")