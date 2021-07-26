from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time
from processImage import processJump
from os import system

driver_name = 'chromedriver.exe'
start_time = time()


def killExistingChromeDriver(name):
    try:
        process = f'taskkill /f /im {name}'
        system(process)
    except:
        pass


def playGame(driver):
    driver.save_screenshot('img.png')
    if processJump(threshold=12.9):
        ActionChains(driver).send_keys(Keys.SPACE).perform()
        print(f"*****Jumped at {time()-start_time}  seconds*****")


killExistingChromeDriver(driver_name)
driver = Chrome(driver_name)
try:
    driver.get('chrome://dino/')
except:
    driver.maximize_window()
    sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    print('Started the Game!')
    sleep(1)
    while True:
        playGame(driver)