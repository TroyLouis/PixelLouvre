from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imageio
import ssl
from PIL import Image

ssl._create_default_https_context = ssl._create_unverified_context

urlToGet = 'https://www.pop.culture.gouv.fr/search/list?ou=%5B%22mus%C3%A9e%20du%20Louvre%22%5D&type=%5B%22tableau%22%5D&image=%5B%22oui%22%5D'
driver = webdriver.Firefox()
driver.get(urlToGet)

def goToNextPage():
    xpathButton1 = '//*[@id=\"__next\"]/div[2]/div/div[3]/div[2]/div[2]/div/div/ul/li[2]/button'
    xpathButton2 = '//*[@id=\"__next\"]/div[2]/div/div[3]/div[2]/div[2]/div/div/ul/li[4]/button'
    doesNextButtonExist = driver.find_elements_by_xpath(xpathButton2)
    element = driver.find_element_by_xpath(xpathButton1)
    if len(doesNextButtonExist) == 0:
        element.click()
    else:
        element = driver.find_element_by_xpath(xpathButton2)
        element.click()

def grabPics():
    for num in range(1,26):
        xPathStart = "//*[@id=\"__next\"]/div[2]/div/div[3]/div[2]/div[2]/div/div/div[2]/div"
        xPathEnd = "/a/div/div[1]/div[1]/img"
        path = xPathStart + str([num]) + xPathEnd
        element = driver.find_element_by_xpath(path)
        imageURL = element.get_attribute('src')
        imageALT = element.get_attribute('alt')
        image = imageio.imread(imageURL)
        folder = '/Users/troy/Desktop/LouvreImages/' + imageALT + '.png'
        imageio.imwrite(folder, image)
        im = Image.open(folder)
        im.save(folder, "JPEG", optimize = True, quality=50)

while True:
    try:
        thumbnail = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "thumbnail"))
        )
    except:
        print("fail")
    grabPics()
    print('25 Images Grabbed')
    goToNextPage()
    print('Next Page')
