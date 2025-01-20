from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

packageName = "com.swaglabsmobileapp"

Screen='test-Username'
username = 'test-Username'
password = 'test-Password'
login = 'test-LOGIN'
menu = 'test-Menu'
cart = 'test-Cart'
filter = 'test-Modal Selector Button'
toggle = 'test-Toggle'
add_to_cart = '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]'
add_to_cart_ios = '(//XCUIElementTypeStaticText[@content-desc="test-ADD TO CART"])[1]'
logout = 'test-LOGOUT'
about = '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Backpack"]'
about_ios = '//XCUIElementTypeStaticText[@content-desc="test-Item title" and @text="Sauce Labs Backpack"]'
sort1 = '//android.widget.TextView[@text="Name (Z to A)"]'
sort1_ios = '//XCUIElementTypeStaticText[@text="Name (Z to A)"]'
sort2 = '//android.widget.TextView[@text="Name (A to Z)"]'
sort2_ios = '//XCUIElementTypeStaticText[@text="Name (A to Z)"]'
checkout = 'test-CHECKOUT'
continue_btn = 'test-CONTINUE'
first_name = "test-First Name"
last_name = "test-Last Name"
zip_code = "test-Zip/Postal Code"
finish = 'test-FINISH'
order_complete = '//android.widget.TextView[@text="THANK YOU FOR YOU ORDER"]'
order_complete_ios = '//XCUIElementTypeStaticText[@text="THANK YOU FOR YOU ORDER"]'

def get_screen(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, Screen)))

def get_username(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, username)))

def get_password(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, password)))

def get_login(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, login)))

def get_menu(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, menu)))

def get_cart(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, cart)))

def get_filter(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, filter)))

def get_toggle(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, toggle)))

def get_addCart(driver,platform_name):
        if platform_name == "Android":
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, add_to_cart)))
        else:
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, add_to_cart_ios)))

def get_logout(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, logout)))

def get_about(driver,platform_name):
        if platform_name == "Android":
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, about)))
        else:
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, about_ios)))

def get_sort(driver,platform_name):
        if platform_name == "Android":
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, sort1)))
        else:
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, sort1_ios)))

def get_sortOriginal(driver,platform_name):
        if platform_name == "Android":
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, sort2)))
        else:
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, sort2_ios)))

def get_checkout(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, checkout)))

def get_continue(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, continue_btn)))

def get_firstname(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, first_name)))

def get_lastname(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, last_name)))

def get_zipcode(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, zip_code)))

def get_finish(driver,platform_name):
        return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, finish)))

def get_orderstatus(driver,platform_name):
        if platform_name == "Android":
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, order_complete)))
        else:
                return WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, order_complete)))