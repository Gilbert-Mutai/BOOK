from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Aluta Travellers'
    sender = 'lutaa0071@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/register-email.txt',{"name": name})
    html_content = render_to_string('email/register-email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def send_admin_email(admin_name,name):
    # Creating message subject and sender
    subject = 'New Member has Joined'
    sender = 'lutaa0071@gmail.com'
    admin_email=['gmutai1194@gmail.com']

    #passing in the context vairables
    text_content = render_to_string('email/admin-email.txt',{"admin_name": admin_name,"name":name})
    html_content = render_to_string('email/admin-email.html',{"admin_name": admin_name,"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,bcc=admin_email)
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_booking_email(name,receiver,station,date,time):
    # Creating message subject and sender
    subject = 'Thank you for Booking'
    sender = 'lutaa0071@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/book-email.txt',{"name": name,"station":station,"date":date,"time":time})
    html_content = render_to_string('email/book-email.html',{"name": name,"station":station,"date":date,"time":time})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()