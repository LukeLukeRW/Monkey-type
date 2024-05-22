from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pyautogui

def initialise():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = 'https://monkeytype.com/'
    driver.get(url)
    return driver

def get_words(driver):
    words = []
    time.sleep(5) #wait to load w p
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    if soup.find('div', id='words'):
        for worddd in soup.find('div', id='words').find_all('div', class_='word'):
            word = ''.join(letter.get_text() for letter in worddd.find_all('letter'))
            words.append(word)
    return words

def main():
    driver = initialise()
    for _ in range(0,2):
        words = get_words(driver)
        text = ' '.join(words);text+=' '
        pyautogui.typewrite(str(text),interval=0.025)
    time.sleep(1000)

if __name__ == '__main__':
    main()
