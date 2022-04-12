"""
    2022 ALL RIGHTS RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created: 08/04/2022 0732hrs EAT

"""
# Using smtplib module to send emails.
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "kelimbth@gmail.com"
receiver_email = "kelimbth@gmail.com"
password = input("Enter your password: ")


message = EmailMessage()
message['From'] = sender_email  # dictionary indexing
message['To'] = receiver_email
message['Subject'] = subject
message.set_content(body)   # set contents of the body in an email

"""
    Formatting email subject and body using HTML
"""
# html = """
#     <html>
#     <body>
#         <h1>{}</h1>
#         <p>{}</p>
#     </body>
#     </html>
# """.format(subject, body)
# message.add_alternative(html, subtype=html)

context = ssl.create_default_context()  # gives a context for a secure connection when using smtplib

print("Sending Email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Success')
