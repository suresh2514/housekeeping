#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:00:06 2020

@author: surkumar
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def gmail_sent(sender="root", receiver="root", password="abc123",subject="System usage Alert", body="test"):
    mail_content = body
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender, password) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    return True
