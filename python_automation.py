# import http requests
from email.mime import text
import requests
# for web scrapping
from bs4 import BeautifulSoup
# Send the mail
import smtplib
# email body
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
