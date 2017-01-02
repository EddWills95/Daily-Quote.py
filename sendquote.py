import time
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import schedule
import urllib2

import config

url = "http://feeds.feedburner.com/quotationspage/qotd"


def getSend():
	file = []
	for i in urllib2.urlopen(url):
		file.append(i)

	titleindicie = [i for i, s in enumerate(file) if "<title>" in s]
	descindicie = [i for i, s in enumerate(file) if "<description" in s]

	rani = random.randint(2, 13)

	authortemp = file[titleindicie[rani]]
	desctemp = file[descindicie[rani]]

	author = authortemp[7:-10]

	quote = desctemp[14:-17]

	host = 'smtp.gmail.com'
	port = 587
	myemail = config.username
	mypassword = config.password

	sendto = config.recipient  # change this later.

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Kirsten's Quote of the Day"
	msg['From'] = myemail
	msg['To'] = sendto

	text = author + '\n' + quote
	html = """\
	<html>
		<head>
			<link href="https://fonts.googleapis.com/css?family=Lora" rel="stylesheet">
		</head>
		<body>
			<div class="text">
				<h1>Good Morning %s</h1>
				<br>
				<h2>I've got a quote for you</h2>
				<br>
				<h2>Random Quotee of the Day:<br><span>%s</span></h2>
				<br>
				<h2>What they said: <br><span>%s</span></h2>
				<br>
				<br>
				<h3><i>Another Quote From <em>Kirsten's Quotes</em></i></h3>
			</div>
		</body>
	</html>
	""" % (name, author, quote)

	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	msg.attach(part1)
	msg.attach(part2)

	print
	"Conecting..."

	server = smtplib.SMTP(host, port)

	server.ehlo()
	server.starttls()

	server.login(myemail, mypassword)

	print
	"Sent"
	server.sendmail(myemail, sendto, msg.as_string())
	server.close()

	file = []


schedule.every().day.at("9:30").do(getSend)

while True:
	schedule.run_pending()
	time.sleep(50)

getSend()
