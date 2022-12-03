from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

def save_image(driver, path):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{now}.png"
    filepath = f"./screenshots/{path}/{filename}"
    driver.save_screenshot(filepath)
    return

@mark.parametrize("nombre,password", [("unavainabien99ad", "5aawd47a"), ("unacosaqauaesitaa", "5aa")])
def test_prueba01_Register(nombre, password):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    time.sleep(4)
    registerElement = driver.find_element(By.XPATH, "//*[@id='signin2']")
    registerElement.click()

    registerName = driver.find_element(By.XPATH, "//*[@id='sign-username']")
    registerName.send_keys(nombre)

    registerPassword = driver.find_element(By.XPATH, "//*[@id='sign-password']")
    registerPassword.send_keys(password)
    save_image(driver, 'register')
    driver.find_element(By.XPATH, "//*[@id='signInModal']//div[@class='modal-footer']/button[2]").click()
    time.sleep(5)
    alert = driver.switch_to.alert.text
    assert alert == 'Sign up successful.'
    driver.close()

@mark.parametrize("nombre,password", [("unacosaquesita", "5a"), ("unacosaquesiaatqqa", "5aaaaqqa")])
def test_prueba02_Login(nombre, password):
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//li/a[@id='login2']").click()

    usernameElement = driver.find_element(By.XPATH, "//input[@id='loginusername']")
    usernameElement.send_keys(nombre)

    passwordElement = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
    passwordElement.send_keys(password)

    save_image(driver, 'login')
    driver.find_element(By.XPATH, "//div[@id='logInModal']//div[@class='modal-footer']/button[2]").click()
    time.sleep(5)

    loginElement = driver.find_element(By.XPATH, "//a[@id='nameofuser']").text
    assert loginElement.__contains__('Welcome')
    driver.close()

def test_prueba03_Phones():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()

    driver.find_element(By.XPATH, '//div[@class="list-group"]/a[2]').click()
    time.sleep(3)
    dataText = driver.find_element(By.XPATH, '//div[@id="tbodyid"]/div[1]/div/div/h4/a').text
    save_image(driver, 'phone')
    assert dataText == 'Samsung galaxy s6'

def test_prueba03_Monitors():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()

    driver.find_element(By.XPATH, '//div[@class="list-group"]/a[4]').click()
    time.sleep(3)
    dataText = driver.find_element(By.XPATH, '//div[@id="tbodyid"]/div[1]/div/div/h4/a').text
    save_image(driver, 'monitors')
    assert dataText == 'Apple monitor 24'

def test_prueba03_Laptop():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")
    driver.maximize_window()

    driver.find_element(By.XPATH, '//*[@id="itemc"][2]').click()
    time.sleep(3)
    dataText = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').text
    save_image(driver, 'laptop')
    assert dataText == 'Sony vaio i5'

