import schedule
import time
import datetime
global quoteNum
import pytz    # $ pip install pytz
import tzlocal # $ pip install tzlocal

quoteNum = []


def job():
	from twilio.rest import Client
	import random
	import json
	import datetime
	account_sid = 'AC9ac3d4a208aed65de2c6a94503b2f29b'
	auth_token = '9b24e7f673c9c1cc22af43cd9820057b'
	client = Client(account_sid, auth_token)
	hour = datetime.datetime.now().hour
	with open("enterpreneur-quotes.json", encoding='utf-8') as handle:
		dictdump = json.loads(handle.read())
		quoteNumber = random.randint(0,len(dictdump))
		print(quoteNumber)
		while(quoteNumber in quoteNum):
			print("ReDraw")
			quoteNumber = random.randint(0,len(dictdump))
		quoteNum.append(quoteNumber)
		x = dictdump[random.randint(0,len(dictdump))]
		quote = x['text']
		author = x['from']
		quoteOfDay = quote + " - " + author
		print(quoteOfDay)
		print(quoteNum)
			message = client.messages.create(
		                              body=quoteOfDay,
		                              from_='+18645394733',
		                              to='2054758001'
		                          )
			message = client.messages.create(
		                              body=quoteOfDay,
		                              from_='+18645394733',
		                              to='2059655555'
		                          )
print(datetime.datetime.now())

schedule.every().day.at("8:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("3:30").do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)


