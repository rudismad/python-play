# import http requests
from email.mime import text
import requests
# for web scrapping
from bs4 import BeautifulSoup
# Send the mail
import smtplib
# email body
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system time and date manipulation
import datetime


now = datetime.datetime.now

# email content placeholder, global variable
content = ''

# extracting hacker news stories


def extract_news(url):

    print('extract hacker news stories')
    # content placeholder
    cnt = ''
    # first line in email body
    cnt += ('<b>HN top stories: <b>\n'+'<br>'+'-'*50+'<br>')
    # Get content from the url
    response = requests.get(url)
    # content of the web page, local variable
    content = response.content
    soup = BeautifulSoup(content, 'html parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text+"\n"+'<br>')
                if tag.text != 'More' else '')
        return (cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>--------------<br>')
content += ('<br><br> End of message')

# lets send an email
print('composing email')

# update your email details

SERVER = 'smtp.gmail.com'  # your email smtp, this one for gmail
PORT = 587  # your port number
FROM = 'gaisais777@gmail.com'  # your email adress you are sending from
TO = 'gaisais777@gmail.com'  # your email adress that receives email
PASS = getpass.getpass('Enter the password:')

#fp=open(file_name, 'rb')
# Create a text/plain message
# msg=MIMEtext('')
msg = MIMEMultipart()

#msg.add_header('Content_Disposition', 'attachment', filename='empty.txt')
msg['Subject'] = 'Top news stories from HN [Automated email]' + \
    ''+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
# fp close()
print('Initiating server')

server = smtplib.SMTP(SERVER, PORT)
# serversmtplib.SMTP SSL('smtp.gmail.com'. 4651)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email sent')
server.quit()
