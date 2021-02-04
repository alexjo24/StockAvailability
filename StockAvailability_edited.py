import sys
from selenium import webdriver
import ezgmail, os
from twilio.rest import Client
import time

def FetchWebsites():


	browser = webdriver.Chrome(executable_path=r'C:\Users\Aleba\Desktop\StockSearch\chromedriver_87.exe')

	loopcc = 0
	while True:

		loopcc += 1
		print("############ Loop: " + str(loopcc) + " ############")
		inetFind(browser)
		komplettFind(browser)


		print("Waiting...")
		time.sleep(100)

	browser.quit()


# def sendMail():
# 	print("SENDING EMAILS!!")
#
# 	# os.chdir(r'C:\Users\Aleba\Desktop\Git_main\StockAvailability')
# 	# ezgmail.init()
# 	nameOfStore = "Inet"
# 	linktmp = "Inet.se" 
# 	bodyText = 'Here is a link: ' + linktmp
# 	ezgmail.send('alexander.jorud@gmail.com', 'Cards in stock@'+nameOfStore, bodyText)


def sendWhatsApp(text):
	#Text must be in format: ['EVGA GeForce RTX 3090 24GB FTW3 ULTRA', 'Gigabyte GeForce RTX 3090 24GB TURBO']
	account_sid = 'FILL IN FROM TWILIO'
	auth_token = 'FILL IN FROM TWILIO'
	client = Client(account_sid, auth_token)
	message_send = ' #### '.join([str(elem) for elem in text])
	message = client.messages.create(
		from_='whatsapp:FILL IN TWILIO NUMBER',
		body=message_send,
		to='whatsapp:FILL IN YOUR PHONE NUMBER'
	)

def inetFind(browser):
	print()
	print("Checking @Inet")
	#To-do
	#Exclude slutsåld...

	isFound = False

	listOfCards = []

	#3080
	browser.get('https://www.inet.se/kategori/167/geforce-gtx-rtx?filters=%7B%2229%22%3A%7B%22type%22%3A%22PropAny%22%2C%22any%22%3A%5B14294%5D%7D%2C%22-2%22%3A%7B%22type%22%3A%22Stock%22%2C%22boolVal%22%3Atrue%7D%7D')
	compare_str = "3080"


	#3090
	#browser.get('https://www.inet.se/kategori/167/geforce-gtx-rtx?filters=%7B%2229%22%3A%7B%22type%22%3A%22PropAny%22%2C%22any%22%3A%5B14294%2C14297%2C14296%5D%7D%2C%22-2%22%3A%7B%22type%22%3A%22Stock%22%2C%22boolVal%22%3Atrue%7D%7D')
	#compare_str = "3090"

	lnks = browser.find_elements_by_tag_name("a")

	for lnk in lnks:

		tmp_list = lnk.text.split(" ")

		if "BOX" not in tmp_list:

			for element in tmp_list:

				if element == compare_str:
					listOfCards.append(lnk.text)
					isFound = True


	if isFound:
		print("Found a card!!!")
		sendWhatsApp(listOfCards)
		print(listOfCards)
	else:
		print("Nothing found @ Inet")


def elgigantenFind():
	pass

def komplettFind(browser):
	print()
	print("Checking @Komplett")
	isFound = False

	listOfCards = []

	#### 3080
	browser.get('https://www.komplett.se/category/10412/datorutrustning/datorkomponenter/grafikkort?nlevel=10000%C2%A728003%C2%A710412&stockStatus=InStock&cnet=Grafikprocessor_A00247%20%20%C2%A7NVIDIA%20GeForce%20RTX%203080')
	compare_str = "3080"


	#### 6900
	# browser.get('https://www.komplett.se/category/10412/datorutrustning/datorkomponenter/grafikkort?nlevel=10000%C2%A728003%C2%A710412&stockStatus=InStock')
	# compare_str = "6900"


	lnks = browser.find_elements_by_tag_name("a")

	cc_amountOfCards = 0
	cc = 0
	for lnk in lnks:
		cc += 1

		tmp_list = lnk.text.split(" ")


		for element in tmp_list:



			if element == compare_str:
				cc_amountOfCards += 1

				if cc_amountOfCards > 1:

					tmp_list2 = lnks[cc + 1].text.split(" ")

					if tmp_list2[0] != 'MEDDELA':

						listOfCards.append(lnk.text)
						isFound = True

	if isFound:
		print("Found a card!!!")
		print(listOfCards)
		sendWhatsApp(listOfCards)
	else:
		print("Nothing found @ Komplett")

def netonnetFind():
	pass

def proshopFind():
	pass

def dustinhomeFind():
	pass

def sweclockersFind():
	pass

def sendEmail():
	pass

def searchFreq():
	pass



if __name__ == '__main__':

	FetchWebsites()
