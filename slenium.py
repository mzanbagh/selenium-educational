#Importing webdriver from selenium library
from selenium import webdriver

#Init chrome web driver with executable path to the driver 
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#getting driver to the website
driver.get("http://www.nytimes.com")
#maximizing window

driver.maximize_window()
#Take and save screen shot as png file

driver.save_screenshot("nytimes_snapshot.png")
#Close the driver

driver.close()
#END