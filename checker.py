import requests
import json
import datetime
import time
token = "TOKEN"
check = ""
while True:
	cookie = dict(sessionid='INSTAGRAM COOKIE')
	req = requests.get('https://i.instagram.com/api/v1/direct_v2/get_presence/', cookies=cookie, headers={'X-IG-App-ID': '936619743392459'}).json()
	status = req['user_presence']['USER ID']['last_activity_at_ms']
	date = datetime.datetime.fromtimestamp(status/1000).strftime('%H:%M %d.%m.%Y')
	if date != check:
		check = date
		requests.get('https://api.telegram.org/bot'+ token + '/sendMessage?chat_id=CHATID&text=' + 'LAST ACTIVITY:\n' + check)
	time.sleep(300)
