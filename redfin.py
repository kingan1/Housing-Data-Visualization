from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path

firefoxProfile = webdriver.FirefoxProfile()
direc = os.getcwd()
firefoxProfile.set_preference("browser.download.panel.shown", False)
firefoxProfile.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/vnd.ms-excel")
firefoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
firefoxProfile.set_preference("browser.download.folderList", 2);
firefoxProfile.set_preference("browser.download.dir", direc)

driver = webdriver.Firefox(firefoxProfile)
driver.get('http://www.redfin.com/city/35711/NC/Raleigh')
driver.find_element_by_class_name("removeIcon").click()
time.sleep(5)
zoomOut = driver.find_element_by_class_name("zoomMinusControlButton")
zoomOut.click()
time.sleep(2)
zoomOut.click()
time.sleep(2)
button = driver.find_element_by_id('download-and-save')
link = button.get_attribute('href')
link = link.replace('350', '10000')
time.sleep(1)
driver.execute_script('arguments[0].setAttribute("href", arguments[1]);', button, link)
button.click()
time.sleep(10)
files = os.listdir()
for f in files:
    if (len(f.split('.')) > 1):
        if f.split('.')[1] == 'csv':
            os.rename(f, 'file.csv')
while not os.path.exists(os.getcwd() + '/file.csv'):
    print('Either file has not been saved or file has been saved incorrectly')
    time.sleep(2)
    files = os.listdir()
    for f in files:
        if (len(f.split('.')) > 1):
            if f.split('.')[1] == 'csv':
               os.rename(f, 'file.csv')

print('done')
driver.close()
