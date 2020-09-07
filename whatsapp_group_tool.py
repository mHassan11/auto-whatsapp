from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# import Action chains  
from selenium.webdriver.common.action_chains import ActionChains 
# import KEYS 
from selenium.webdriver.common.keys import Keys 

import time
from pathlib import Path

options = Options()
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')

def send_message(name, msg):
	flag = True

	try:
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		# print("trying")
		user.click()

		# print("Writing msg")
		wait = WebDriverWait(driver = driver, timeout = 90)
		time.sleep(10)
		msg_box = driver.find_element_by_class_name('_3uMse')
		msg_box.send_keys(msg)
		# msg_box.send_keys(Keys.SHIFT+Keys.ENTER)
		# ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
		
		# create action chain object 
		# action = ActionChains(driver)
		# perform the oepration 
		# action.key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.CONTROL).perform() 

		# msg_box.send_keys("Automated Message")
		# print("here, done typing")

		# print("Pressing send button")
		time.sleep(5)
		wait = WebDriverWait(driver = driver, timeout = 90)
		button = driver.find_element_by_class_name('_1U1xa')
		button.click()

	except:
		flag = False
		return False
		
	return flag

#####
name_list = ['hassan', 'Group1']
msg = "hello1"

with open('arguments.txt') as f:
    arg_list = [line.rstrip() for line in f]

msg_file = arg_list[0]+'.txt'
contact_file = arg_list[1]+'.txt'

break_line = "                                                  "
brk_line = break_line + break_line + break_line
with open(msg_file) as f:
	msg = brk_line.join([x.strip() for x in f]) 
# print(msg)

with open(contact_file) as f:
    name_list = [line.rstrip() for line in f]
# print(name_list)

swait = WebDriverWait(driver = driver, timeout = 900)
time.sleep(30)

for name in name_list:
	# print(name)
	resp = send_message(name, msg)
	if(resp == False):
		# print("Not done->", name,". Will try again")
		name = name_list.append(name)
	else:
		# pass
		print("Done->", name)

time.sleep(5)
driver.close()