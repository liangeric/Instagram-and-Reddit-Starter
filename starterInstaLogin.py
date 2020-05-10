# In order for this work make sure safari allows remote automation 
# (this can be turned on in safari under the develop tab)

# Import what we will be using for this code
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginBrowser:

	# this creates the login browser
	def __init__(self,url):		
		# create a safari browser
		self.browser = webdriver.Safari()

		# resize the window the appropriate pixel size
		self.browser.set_window_size(1264,699)

		# go to instagram web page
		self.browser.get(url)

	#this does the log in with the given information
	def login(self,myuser,mypass):
		# find on the page where it requires the user to enter log in information
		# if this times out that means intenet connection might be slow or not working
		# increase the time 10 to a larger number in this case or test internet speed
		username = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.NAME,"username")))
		password = self.browser.find_element_by_name('password')

		# This types in the username and password into the web browser
		username.send_keys(myuser)
		password.send_keys(mypass)

		# This finds the log in button and clicks it, which would log the user 
		# into their instagram account
		submit = self.browser.find_element_by_xpath("//button[@type='submit']")
		submit.click()

	def close(self):
		self.browser.close()

# test browser functions
page = LoginBrowser("https://www.instagram.com/")
# replace with your username and password
page.login("user","pass")
# uncomment this line to automatically close the page for yourself
# page.close()























