from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import time


# This app finds best build for every League of Legends champion, by scraping lolalytics.com & getting around Riot Games API
# Remember to update Chromium or change code to use webdriver_manager.chrome

def check(champion = input('Pick your Champion:\n').lower(), mode = input('Pick your game mode:\n')):
    mode = mode.replace(' ','').lower()
    if len(mode) < 1 or mode == 'sr' or mode == 'summonersrift':
        PATH = 'C:\Program Files\chromedriver.exe' # Enter your chromium location here
        driver = webdriver.Chrome(PATH)
        driver.get(f'https://lolalytics.com/lol/{champion}/build/')
        print(driver.title) 
        print(champion)
        try:
            accept = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ncmp__btn'))
            )
            accept.click()
            accept = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="ncmp__btn ncmp__btn-danger"]'))
            )
            accept.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 250)")
            nazwa = f'{champion}.png'
            driver.save_screenshot(nazwa)
            obraz = Image.open(nazwa, mode='r')
            obraz.show()
        finally:
            driver.quit()
    else:
        PATH = 'C:\Program Files\chromedriver.exe'
        driver = webdriver.Chrome(PATH)
        driver.get(f'https://lolalytics.com/lol/{champion}/{mode}/build/')
        print(driver.title) 
        print(champion)
        try:
            accept = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ncmp__btn'))
            )
            accept.click()
            accept = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@class="ncmp__btn ncmp__btn-danger"]'))
            )
            accept.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 250)")
            nazwa = f'{champion}.png'
            driver.save_screenshot(nazwa)
            obraz = Image.open(nazwa, mode='r')
            obraz.show()
        finally:
            driver.quit()

check() # Calling the function


