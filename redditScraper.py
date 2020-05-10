# In order for this work make sure safari allows remote automation 
# (this can be turned on in safari under the develop tab)

# Import what we will be using for this code
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class homeBrowser:

	# this creates the home browser
	def __init__(self,url):		
		# create a safari browser
		self.browser = webdriver.Safari()

		# resize the window the appropriate pixel size
		self.browser.set_window_size(1264,699)

		# go to web page
		self.browser.get(url)

	# navigate to the appropriate/closest subreddit from reddit homepage
	def navigateSub(self,subName):
		# find the search bar
		# if this times out that means intenet connection might be slow or not working
		# increase the time 10 to a larger number in this case or test internet speed
		searchBar = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,"header-search-bar")))

		# enter the subreddit you are looking for in the search bar
		searchBar.send_keys(subName)
		searchBar.send_keys(Keys.RETURN)

		# navigate/filter to the subreddits tab
		subs = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,
			"//*[contains(text(), 'Communities and users')]")))
		subs.click()

		# select the first option
		first = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,
			"//*[contains(text(), 'r/')]")))
		first.click()

	# toggle the user tab
	def userToggle(self):
		user = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,
			"USER_DROPDOWN_ID")))
		user.click()

	# toggle reddit dark mode
	def darkMode(self):
		self.userToggle()
		mode = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,
			"//*[contains(text(), 'Night Mode')]")))
		mode.click()

	def close(self):
		self.browser.close()

# test browser functions
page = homeBrowser("https://www.reddit.com")

# navigate to a subreddit you are looking for
page.navigateSub("jokes")

# uncomment this line to automatically turn on dark mode for reddit
# page.darkMode()

# uncomment this line to automatically close the page for yourself
# page.close()























