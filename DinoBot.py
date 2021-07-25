from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from processImage import processJump

driver = Chrome('chromedriver.exe')

canvas_css = 'div.runner-container[role="application"]'


def playGame(driver):
    canvas = driver.find_element_by_css_selector(canvas_css)
    canvas.screenshot('img.png')
    if processJump(threshold=12.8):
        ActionChains(driver).send_keys(Keys.SPACE).perform()
        print("Jumped")


try:
    driver.get('https://google.com')
except:
    driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    print('Started the Game!')
    sleep(1)
    while True:
        playGame(driver)