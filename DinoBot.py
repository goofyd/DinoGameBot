from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time
from processImage import processJump
from os import system

driver_name = 'chromedriver.exe'
start_time = time()
canvas_css = 'div.runner-container[role="application"]'

driver = Chrome(driver_name)


def killExistingChromeDriver(name):
    try:
        process = f'taskkill /f /im {name}'
        system(process)
    except:
        pass


def playGame(driver):
    canvas = driver.find_element_by_css_selector(canvas_css)
    canvas.screenshot('img.png')
    if processJump(threshold=12.8):
        ActionChains(driver).send_keys(Keys.SPACE).perform()
        print(f"Jumped at {time()-start_time} seconds")


try:

    killExistingChromeDriver(driver_name)
    driver.get('https://google.com')
except:
    driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    print('Started the Game!')
    sleep(1)
    while time()-start_time < 60:
        playGame(driver)
    driver.quit()