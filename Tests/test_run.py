import subprocess
from appium import webdriver
import os, sys, pytest, allure, time
from allure import attachment_type
from airtest.core.api import *
# So that we can run this file from anywhere
workingDir =os.path.dirname(os.path.dirname(__file__))
sys.path.append(workingDir)
print(workingDir)
from appium.options.android import UiAutomator2Options
import traceback
import Objects.Swaglab_objects as slo



desired_caps = {
    # For Android 
    'platformName' : 'Android',
    'deviceName' : 'emulator-5554',
	'platformVersion' : '11',
    # For iOS
  	# 'platform' ='iOS',
    # 'deviceid' = '192.168.5.60' 
}
# For Android
options = UiAutomator2Options().load_capabilities(desired_caps)
# For iOS
# options = xcuitest().load_capabilities(desired_caps)

platform_name = "Android"  # Change to "ios" for iOS testing
command_executor = "http://127.0.0.1:4723/wd/hub"

print("Test started")
driver = webdriver.Remote(options=options, command_executor=command_executor)

'''Test scripts to run'''

@allure.description("Check whether the application is installed or not.\n If not then, install the same")
def test_app():
	is_app_installed=driver.is_app_installed(slo.packageName)
	allure.attach(driver.get_screenshot_as_png(),name="App",attachment_type=attachment_type.PNG)
	try:
		if not is_app_installed:
			print("apk is not installed on the device. \nNow installing the apk to the device ...")
			path = "./Apk/SauceLabs.apk"
			if platform_name == "Android":
				# To install apk to Android device
				subprocess.run(f"adb -s emulator-5554 install {path}", shell=True) # installing the app
			else:
				# To install ipa to iOS device
				subprocess.run(f"ideviceinstaller -u 192.168.5.60 -i {path}", shell=True)
			time.sleep(60)
		else:
			print("apk is already installed on the device")
		print("Activating the app")
		driver.activate_app(slo.packageName) 
		slo.get_screen(driver,platform_name)
		# assert exists(Template("./images/RemoveAds.png"))
		allure.attach(driver.get_screenshot_as_png(),name="AppLobby",attachment_type=attachment_type.PNG)
		print("Lobby successfully launched")
	except Exception as e:
		print(e)
		traceback.print_exc()


@allure.description("Login to the application")
def test_login():
	username="standard_user"
	password="secret_sauce"
	try:
		allure.attach(driver.get_screenshot_as_png(),name="AppLobby",attachment_type=attachment_type.PNG)
		print("Now, I am trying to log into the app")
		id = slo.get_username(driver,platform_name)
		id.send_keys(username)
		print("Username entered")
		passcode = slo.get_password(driver,platform_name)
		passcode.send_keys(password)
		print("Password entered")
		login_button = slo.get_login(driver,platform_name)
		login_button.click()
		print("Login button clicked")
		time.sleep(5)
		allure.attach(driver.get_screenshot_as_png(),name="Logged in",attachment_type=attachment_type.PNG)
	except Exception as e:
		print(e)
		traceback.print_exc()


@allure.description("Placing the order")
def test_menu():
	try:
		allure.attach(driver.get_screenshot_as_png(),name="Lobby",attachment_type=attachment_type.PNG)
		menu = slo.get_menu(driver,platform_name)
		menu.click()
		about = slo.get_about(driver,platform_name)
		about.click()
		print("Clicking the About on menu")
		allure.attach(driver.get_screenshot_as_png(),name="About",attachment_type=attachment_type.PNG)
		driver.execute_script('mobile: shell', {'command': 'input','args': ['keyevent', '4']})
		toggle = slo.get_toggle(driver,platform_name)
		toggle.click()
		allure.attach(driver.get_screenshot_as_png(),name="Toggle",attachment_type=attachment_type.PNG)
		time.sleep(3)
		toggle.click()
		filter = slo.get_filter(driver,platform_name)
		filter.click()
		allure.attach(driver.get_screenshot_as_png(),name="Filter",attachment_type=attachment_type.PNG)
		sort = slo.get_sort(driver,platform_name)
		sort.click()
		print("Sort the products")
		allure.attach(driver.get_screenshot_as_png(),name="Filtered Sequence",attachment_type=attachment_type.PNG)
		filter = slo.get_filter(driver,platform_name)
		filter.click()
		sort = slo.get_sortOriginal(driver,platform_name)
		sort.click()
		addItem = slo.get_addCart(driver,platform_name)
		allure.attach(driver.get_screenshot_as_png(),name="Add to cart",attachment_type=attachment_type.PNG)
		addItem.click()
		print("Add item to cart to place order")
		cart = slo.get_cart(driver,platform_name)
		cart.click()
		time.sleep(5)
		driver.swipe(400,1100,400,600)
		checkout = slo.get_checkout(driver,platform_name)
		allure.attach(driver.get_screenshot_as_png(),name="Checkout",attachment_type=attachment_type.PNG)
		checkout.click()
		print("Entering the checkout details")
		first_name = slo.get_firstname(driver,platform_name)
		first_name.send_keys("test")
		last_name = slo.get_lastname(driver,platform_name)
		last_name.send_keys("user")
		pin = slo.get_zipcode(driver,platform_name)
		pin.send_keys('100101')
		allure.attach(driver.get_screenshot_as_png(),name="Order details",attachment_type=attachment_type.PNG)
		continue_button = slo.get_continue(driver,platform_name)
		continue_button.click()
		time.sleep(5)
		driver.swipe(433,1004,433,350)
		finish = slo.get_finish(driver,platform_name)
		finish.click()
		order_status = slo.get_orderstatus(driver,platform_name)
		print(f"Status of the order : ",order_status.text)
		time.sleep(3)
		allure.attach(driver.get_screenshot_as_png(),name="Order Completed",attachment_type=attachment_type.PNG)
	except Exception as e:
		print(e)
		traceback.print_exc()

@allure.description("Logout the application")
def test_logout():
	try:
		print("Trying to logout")
		menu = slo.get_menu(driver,platform_name)
		menu.click()
		logout = slo.get_logout(driver,platform_name)
		logout.click()
		allure.attach(driver.get_screenshot_as_png(),name="Clicking Logout",attachment_type=attachment_type.PNG)
		print("Logout completed")
		time.sleep(3)
		allure.attach(driver.get_screenshot_as_png(),name="Logout",attachment_type=attachment_type.PNG)
	except Exception as e:
		print(e)
		traceback.print_exc()
	driver.quit()