import telebot
import time
import random
import requests
import telebot
import random
import os
from time import sleep
from telebot import types
owner = [1972]
private = [-674191525]

bot = telebot.TeleBot("5073845264:AAEsrDC1SrAJgUSn5D_w5WJ3YsbBG4jrhrg")

@ bot . message_handler ( commands = ['start']) 
def  send_welcome ( message ):
	 if message.from_user.id in owner:
	 	first = message.from_user.first_name
	 	bot.reply_to(message,f"""welcome {first} to bot
To see the functionality of the bot, click /help
... ... ... ... ... ... ...
bot with @D_4_X""",)
	 if message.from_user.id in private:
	 	first = message.from_user.first_name
	 	bot.reply_to(message,f"""welcome {first} to bot
To see the functionality of the bot, click /help
... ... ... ... ... ... ...
bot with @D_4_X""",)
	 if message.from_user.id not in private and message.from_user.id not in owner:
	 	bot.reply_to(message,f'''Ahh.. shit here we go again

Error: Unauthorised Access
CONTACT : @D_4_X''')


@ bot . message_handler ( commands = ['idgroub']) 
def  id_groub ( message ):
	 try:
	 	id = message.chat.id
	 	bot.reply_to(message,id)
	 except:
	 	pass

@ bot . message_handler ( commands = ['help']) 
def  send_welcome ( message ):
	 if message.from_user.id in owner:
	 	bot.reply_to(message,f"""
1- if you want check sk send-
/key + sk
2 - if you want check visa send-
/ch + visa
3 - if you want check bin send-
/bin + bin
... ... ... ... ... ... ...
BOT MADE BY : @D_4_X""",)
	 if message.from_user.id in private:
	 	bot.reply_to(message,f"""
1- if you want check sk send-
/key + sk
2 - if you want check visa send-
/ch + visa
3 - if you want check bin send-
/bin + bin
... ... ... ... ... ... ...
BOT MADE BY : @D_4_X""",)
	 if message.from_user.id not in private and message.from_user.id not in owner:
	 	bot.reply_to(message,f'''Ahh.. shit here we go again

Error: Unauthorised Access
CONTACT : @D_4_X''')


@bot.message_handler(func=lambda message:True)
def msg(message):
	if message.chat.type == 'private':
		if message.from_user.id in owner:
			c = message.text
			if '/key ' in c:
				skk = c.replace('/key ','')
				try:
					bot.delete_message(message.chat.id,message.message_id)
					url = f"https://khafeer.ml/secret-key/checker-sk.php?sk={skk}"
					rel = requests.get(url)
					res = rel.json()
					ssk = res["sk"]
					response = res["message"]
					idd = message.from_user.id
					first = message.from_user.first_name
					if 'Live Key' in response:
						bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS LIVE ✅
│•┞ CHECKED BY » {first}({idd})[OWNER😈]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ✅
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
					else:
						bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS DEAD ❎ 
│•┞ CHECKED BY » {first}({idd})[OWNER😈]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ❎
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
				except:
					pass
			if '/ch ' in c:
				try:
					idd = message.from_user.id
					first = message.from_user.first_name
					visa = c.replace('/ch ','')
					url = f"https://khafeer.ml/CVV/cc3.php?card={visa}"
					rel = requests.get(url)
					res = rel.json()
					cc = res["cc"]
					status = res["status"]
					response = res["response"]
					gateaway = res["gateaway"]
					bin = res["card_details"]["bin"]
					scheme = res["card_details"]["scheme"]
					type = res["card_details"]["type"]
					category = res["card_details"]["category"]
					country = res["card_details"]["country"]
					emoji = res["card_details"]["emoji"]
					country_code = res["card_details"]["country_code"]
					country_currency = res["card_details"]["country_currency"]
					bank = res["card_details"]["bank"]
					bank_url = res["card_details"]["bank_url"]
					bank_phone = res["card_details"]["bank_phone"]
					bot.reply_to(message,f"""۞ ------------ ⫷ CARD ⫸ ------------ ۞
◈ CC: {cc}
◈ Status: {status}
◈ response: {response}
◈ gateaway: {gateaway}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Bin: {bin}
◈ scheme: {scheme}
◈ type: {type}
◈ category: {category} 
◈ country:  {country}
◈ emoji:  {emoji}
◈ country_code: {country_code}
◈ country_currency: {country_currency}
◈ bank: {bank}
◈ bank_url: {bank_url}
◈ bank phone: {bank_phone}
۞ ------------ ⫷ DATA ⫸ ------------ ۞
◈ Checked By: {first}({idd})[OWNER😈]
◈ BOT MADE BY : @D_4_X""")
				except:
					pass


			if '/bin ' in c:
				try:
					idd = message.from_user.id
					first = message.from_user.first_name
					bin = c.replace('/bin ','')
					url = f"https://bins-su-api.now.sh/api/{bin}"
					rel = requests.get(url)
					res = rel.json()
					vendor = res['data']['vendor']
					typee = res['data']['type']
					level = res['data']['level']
					bank = res['data']['bank']
					dialCode = res['data']['countryInfo']['dialCode']
					code = res['data']['countryInfo']['code']
					emoji = res['data']['countryInfo']['emoji']
					country = res['data']['country']
					bot.reply_to(message,f"""BIN INFO 🔥
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ BɪN : {bin}
◈ TʏPᴇ : {typee}
◈ LᴇVᴇL : {level}
◈ BᴀNᴋ : {bank}
◈ CᴏUɴᴛRʏ : {country}{emoji}
◈ VᴇɴDᴏR : {vendor}
◈ CᴏDᴇ : {dialCode} {code}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Checked By: {first}({idd})[OWNER😈]
◈ BOT MADE BY : @D_4_X""")
				except:
					pass
		if message.from_user.id in private:
			c = message.text
			if '/key ' in c:
				skk = c.replace('/key ','')
				try:
					bot.delete_message(message.chat.id,message.message_id)
					url = f"https://khafeer.ml/secret-key/checker-sk.php?sk={skk}"
					rel = requests.get(url)
					res = rel.json()
					ssk = res["sk"]
					response = res["message"]
					idd = message.from_user.id
					first = message.from_user.first_name
					if 'Live Key' in response:
						bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS LIVE ✅
│•┞ CHECKED BY » {first}({idd})[PREMIUM USER 🔥]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ✅
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
					else:
						bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS DEAD ❎ 
│•┞ CHECKED BY » {first}({idd})[PREMIUM USER 🔥]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ❎
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
				except:
					pass
			if '/ch ' in c:
				try:
					idd = message.from_user.id
					first = message.from_user.first_name
					visa = c.replace('/ch ','')
					url = f"https://khafeer.ml/CVV/cc3.php?card={visa}"
					rel = requests.get(url)
					res = rel.json()
					cc = res["cc"]
					status = res["status"]
					response = res["response"]
					gateaway = res["gateaway"]
					bin = res["card_details"]["bin"]
					scheme = res["card_details"]["scheme"]
					type = res["card_details"]["type"]
					category = res["card_details"]["category"]
					country = res["card_details"]["country"]
					emoji = res["card_details"]["emoji"]
					country_code = res["card_details"]["country_code"]
					country_currency = res["card_details"]["country_currency"]
					bank = res["card_details"]["bank"]
					bank_url = res["card_details"]["bank_url"]
					bank_phone = res["card_details"]["bank_phone"]
					bot.reply_to(message,f"""۞ ------------ ⫷ CARD ⫸ ------------ ۞
◈ CC: {cc}
◈ Status: {status}
◈ response: {response}
◈ gateaway: {gateaway}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Bin: {bin}
◈ scheme: {scheme}
◈ type: {type}
◈ category: {category} 
◈ country:  {country}
◈ emoji:  {emoji}
◈ country_code: {country_code}
◈ country_currency: {country_currency}
◈ bank: {bank}
◈ bank_url: {bank_url}
◈ bank phone: {bank_phone}
۞ ------------ ⫷ DATA ⫸ ------------ ۞
◈ Checked By: {first}({idd})[PREMIUM USER 🔥]
◈ BOT MADE BY : @D_4_X""")
				except:
					pass


			if '/bin ' in c:
				try:
					idd = message.from_user.id
					first = message.from_user.first_name
					bin = c.replace('/bin ','')
					url = f"https://bins-su-api.now.sh/api/{bin}"
					rel = requests.get(url)
					res = rel.json()
					vendor = res['data']['vendor']
					typee = res['data']['type']
					level = res['data']['level']
					bank = res['data']['bank']
					dialCode = res['data']['countryInfo']['dialCode']
					code = res['data']['countryInfo']['code']
					emoji = res['data']['countryInfo']['emoji']
					country = res['data']['country']
					bot.reply_to(message,f"""BIN INFO 🔥
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ BɪN : {bin}
◈ TʏPᴇ : {typee}
◈ LᴇVᴇL : {level}
◈ BᴀNᴋ : {bank}
◈ CᴏUɴᴛRʏ : {country}{emoji}
◈ VᴇɴDᴏR : {vendor}
◈ CᴏDᴇ : {dialCode} {code}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Checked By: {first}({idd})[PREMIUM USER 🔥]
◈ BOT MADE BY : @D_4_X""")
				except:
					pass
		if message.from_user.id not in private and message.from_user.id not in owner:
			bot.reply_to(message,f'''Ahh.. shit here we go again

Error: Unauthorised Access
CONTACT : @D_4_X''')
	if message.chat.type == "group" or message.chat.type == "supergroup":
		if message.chat.id in private:
			if message.from_user.id in owner:
				c = message.text
				if '/key ' in c:
					skk = c.replace('/key ','')
					try:
						bot.delete_message(message.chat.id,message.message_id)
						url = f"https://khafeer.ml/secret-key/checker-sk.php?sk={skk}"
						rel = requests.get(url)
						res = rel.json()
						ssk = res["sk"]
						response = res["message"]
						first = message.from_user.first_name
						idd = message.from_user.id
						if 'Live Key' in response:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS LIVE ✅
│•┞ CHECKED BY » {first}({idd})[OWNER😈]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ✅
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
						else:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS DEAD ❎ 
│•┞ CHECKED BY » {first}({idd})[OWNER😈]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ❎
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
					except:
						pass
				if '/ch ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						visa = c.replace('/ch ','')
						url = f"https://khafeer.ml/CVV/cc3.php?card={visa}"
						rel = requests.get(url)
						res = rel.json()
						cc = res["cc"]
						status = res["status"]
						response = res["response"]
						gateaway = res["gateaway"]
						bin = res["card_details"]["bin"]
						scheme = res["card_details"]["scheme"]
						type = res["card_details"]["type"]
						category = res["card_details"]["category"]
						country = res["card_details"]["country"]
						emoji = res["card_details"]["emoji"]
						country_code = res["card_details"]["country_code"]
						country_currency = res["card_details"]["country_currency"]
						bank = res["card_details"]["bank"]
						bank_url = res["card_details"]["bank_url"]
						bank_phone = res["card_details"]["bank_phone"]
						bot.reply_to(message,f"""۞ ------------ ⫷ CARD ⫸ ------------ ۞
◈ CC: {cc}
◈ Status: {status}
◈ response: {response}
◈ gateaway: {gateaway}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Bin: {bin}
◈ scheme: {scheme}
◈ type: {type}
◈ category: {category} 
◈ country:  {country}
◈ emoji:  {emoji}
◈ country_code: {country_code}
◈ country_currency: {country_currency}
◈ bank: {bank}
◈ bank_url: {bank_url}
◈ bank phone: {bank_phone}
۞ ------------ ⫷ DATA ⫸ ------------ ۞
◈ Checked By: {first}({idd})[OWNER😈]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass


				if '/bin ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						bin = c.replace('/bin ','')
						url = f"https://bins-su-api.now.sh/api/{bin}"
						rel = requests.get(url)
						res = rel.json()
						vendor = res['data']['vendor']
						typee = res['data']['type']
						level = res['data']['level']
						bank = res['data']['bank']
						dialCode = res['data']['countryInfo']['dialCode']
						code = res['data']['countryInfo']['code']
						emoji = res['data']['countryInfo']['emoji']
						country = res['data']['country']
						bot.reply_to(message,f"""BIN INFO 🔥
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ BɪN : {bin}
◈ TʏPᴇ : {typee}
◈ LᴇVᴇL : {level}
◈ BᴀNᴋ : {bank}
◈ CᴏUɴᴛRʏ : {country}{emoji}
◈ VᴇɴDᴏR : {vendor}
◈ CᴏDᴇ : {dialCode} {code}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Checked By: {first}({idd})[OWNER😈]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass
			if message.from_user.id in private:
				c = message.text
				if '/key ' in c:
					skk = c.replace('/key ','')
					try:
						bot.delete_message(message.chat.id,message.message_id)
						url = f"https://khafeer.ml/secret-key/checker-sk.php?sk={skk}"
						rel = requests.get(url)
						res = rel.json()
						ssk = res["sk"]
						response = res["message"]
						first = message.from_user.first_name
						idd = message.from_user.id
						if 'Live Key' in response:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS LIVE ✅
│•┞ CHECKED BY » {first}({idd})[PREMIUM USER 🔥]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ✅
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
						else:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS DEAD ❎ 
│•┞ CHECKED BY » {first}({idd})[PREMIUM USER 🔥]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ❎
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
					except:
						pass
				if '/ch ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						visa = c.replace('/ch ','')
						url = f"https://khafeer.ml/CVV/cc3.php?card={visa}"
						rel = requests.get(url)
						res = rel.json()
						cc = res["cc"]
						status = res["status"]
						response = res["response"]
						gateaway = res["gateaway"]
						bin = res["card_details"]["bin"]
						scheme = res["card_details"]["scheme"]
						type = res["card_details"]["type"]
						category = res["card_details"]["category"]
						country = res["card_details"]["country"]
						emoji = res["card_details"]["emoji"]
						country_code = res["card_details"]["country_code"]
						country_currency = res["card_details"]["country_currency"]
						bank = res["card_details"]["bank"]
						bank_url = res["card_details"]["bank_url"]
						bank_phone = res["card_details"]["bank_phone"]
						bot.reply_to(message,f"""۞ ------------ ⫷ CARD ⫸ ------------ ۞
◈ CC: {cc}
◈ Status: {status}
◈ response: {response}
◈ gateaway: {gateaway}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Bin: {bin}
◈ scheme: {scheme}
◈ type: {type}
◈ category: {category} 
◈ country:  {country}
◈ emoji:  {emoji}
◈ country_code: {country_code}
◈ country_currency: {country_currency}
◈ bank: {bank}
◈ bank_url: {bank_url}
◈ bank phone: {bank_phone}
۞ ------------ ⫷ DATA ⫸ ------------ ۞
◈ Checked By: {first}({idd})[PREMIUM USER 🔥]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass


				if '/bin ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						bin = c.replace('/bin ','')
						url = f"https://bins-su-api.now.sh/api/{bin}"
						rel = requests.get(url)
						res = rel.json()
						vendor = res['data']['vendor']
						typee = res['data']['type']
						level = res['data']['level']
						bank = res['data']['bank']
						dialCode = res['data']['countryInfo']['dialCode']
						code = res['data']['countryInfo']['code']
						emoji = res['data']['countryInfo']['emoji']
						country = res['data']['country']
						bot.reply_to(message,f"""BIN INFO 🔥
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ BɪN : {bin}
◈ TʏPᴇ : {typee}
◈ LᴇVᴇL : {level}
◈ BᴀNᴋ : {bank}
◈ CᴏUɴᴛRʏ : {country}{emoji}
◈ VᴇɴDᴏR : {vendor}
◈ CᴏDᴇ : {dialCode} {code}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Checked By: {first}({idd})[PREMIUM USER 🔥]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass
			if message.from_user.id not in private and message.from_user.id not in owner:
				c = message.text
				if '/key ' in c:
					skk = c.replace('/key ','')
					try:
						bot.delete_message(message.chat.id,message.message_id)
						url = f"https://khafeer.ml/secret-key/checker-sk.php?sk={skk}"
						rel = requests.get(url)
						res = rel.json()
						ssk = res["sk"]
						response = res["message"]
						first = message.from_user.first_name
						idd = message.from_user.id
						if 'Live Key' in response:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS LIVE ✅
│•┞ CHECKED BY » {first}({idd})[FREE USER 🥲]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ✅
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
						else:
							bot.send_message(message.chat.id,f"""╭————————————
│•╭━─━─━─━─━─━─━╮
│•┞ SK IS DEAD ❎ 
│•┞ CHECKED BY » {first}({idd})[FREE USER 🥲]
│•┞━─━─━─━─━─━─━╯
│•╽
│•┞ KEY » {ssk}
│•┞ Response » {response} ❎
│•╽
│•┞━─━─━─━─━─━╮
│•┞ BOT BY ➺  @D_4_X
│•╰━─━─━─━─━─━╯
╰————————————
-""")
					except:
						pass
				if '/ch ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						visa = c.replace('/ch ','')
						url = f"https://khafeer.ml/CVV/cc3.php?card={visa}"
						rel = requests.get(url)
						res = rel.json()
						cc = res["cc"]
						status = res["status"]
						response = res["response"]
						gateaway = res["gateaway"]
						bin = res["card_details"]["bin"]
						scheme = res["card_details"]["scheme"]
						type = res["card_details"]["type"]
						category = res["card_details"]["category"]
						country = res["card_details"]["country"]
						emoji = res["card_details"]["emoji"]
						country_code = res["card_details"]["country_code"]
						country_currency = res["card_details"]["country_currency"]
						bank = res["card_details"]["bank"]
						bank_url = res["card_details"]["bank_url"]
						bank_phone = res["card_details"]["bank_phone"]
						bot.reply_to(message,f"""۞ ------------ ⫷ CARD ⫸ ------------ ۞
◈ CC: {cc}
◈ Status: {status}
◈ response: {response}
◈ gateaway: {gateaway}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Bin: {bin}
◈ scheme: {scheme}
◈ type: {type}
◈ category: {category} 
◈ country:  {country}
◈ emoji:  {emoji}
◈ country_code: {country_code}
◈ country_currency: {country_currency}
◈ bank: {bank}
◈ bank_url: {bank_url}
◈ bank phone: {bank_phone}
۞ ------------ ⫷ DATA ⫸ ------------ ۞
◈ Checked By: {first}({idd})[FREE USER 🥲]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass


				if '/bin ' in c:
					try:
						first = message.from_user.first_name
						idd = message.from_user.id
						bin = c.replace('/bin ','')
						url = f"https://bins-su-api.now.sh/api/{bin}"
						rel = requests.get(url)
						res = rel.json()
						vendor = res['data']['vendor']
						typee = res['data']['type']
						level = res['data']['level']
						bank = res['data']['bank']
						dialCode = res['data']['countryInfo']['dialCode']
						code = res['data']['countryInfo']['code']
						emoji = res['data']['countryInfo']['emoji']
						country = res['data']['country']
						bot.reply_to(message,f"""BIN INFO 🔥
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ BɪN : {bin}
◈ TʏPᴇ : {typee}
◈ LᴇVᴇL : {level}
◈ BᴀNᴋ : {bank}
◈ CᴏUɴᴛRʏ : {country}{emoji}
◈ VᴇɴDᴏR : {vendor}
◈ CᴏDᴇ : {dialCode} {code}
۞ ------------- ⫷ BIN ⫸ ------------- ۞
◈ Checked By: {first}({idd})[FREE USER 🥲]
◈ BOT MADE BY : @D_4_X""")
					except:
						pass

		if message.chat.id not in groub:
			bot.reply_to(message,f'''Ahh.. shit here we go again

Error: Unauthorised Access
CONTACT : @D_4_X''')

bot.polling(True)
