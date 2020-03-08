from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from behave import *


# host = '0.0.0.0' #os.environ['0.0.0.0']
# port = 4444 #os.environ['4444']
from selenium import webdriver

# iPhone
# driver = webdriver.Remote('http://127.0.0.1:4444')
driver = webdriver.Chrome()
# Android
# driver = webdriver.Remote(browser_name="android", command_executor='http://127.0.0.1:8080/hub')

# Google Chrome
# driver = webdriver.Chrome()

# Firefox
# driver = webdriver.Firefox()


def before_all(context):
	# desired_capabilities = webdriver.DesiredCapabilities
	# desired_capabilities['version'] = 'latest'
	# desired_capabilities['platform'] = 'WINDOWS'
	# desired_capabilities['name'] = 'Testing Selenium with Behave'
	# desired_capabilities['client_key'] = 'key'
	# desired_capabilities['client_secret'] = 'secret'
	# chrome_options = Options()
	# chrome_options.add_argument("--disable-extensions")
	# driver = webdriver.Chrome(chrome_options=chrome_options)
	# chrome_options.add_argument('--no-sandbox')
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--no-sandbox")
	chrome_options.add_argument("--verbose")
	chrome_options.add_argument("--log-path=chrome.log")
	chrome_options.add_argument("window-size=1200x600")
	chrome_options.add_argument("user-data-dir=\\")
	context.browser = webdriver.Chrome(chrome_options=chrome_options)
	# context.browser = webdriver.Remote( #"http://127.0.0.1:4444"
	# 	desired_capabilities=None,
	# 		command_executor="http://127.0.0.1:4444",
	# context.browser = browser = webdriver.Chrome();
	# context.browser = webdriver.Remote(browser_name="Chrome", command_executor='http://127.0.0.1:4444/hub')

	pass

def after_all(context):
	print(context)
	if context is not None:
		context.browser.quit()
