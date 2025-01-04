from functions import not_following
import selenium.webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


persons = not_following()
driver = selenium.webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(4)

usr = driver.find_element(By.NAME,'username')
usr.send_keys('your username')
passw = driver.find_element(By.NAME,'password')
passw.send_keys('your password')
passw.send_keys(Keys.ENTER)
time.sleep(4)

count = 0
for person in persons:
    driver.get('https://www.instagram.com/{}'.format(person))
    time.sleep(2)
   
    
    try:
        following = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button/div/div[1]')
        following.click()
        time.sleep(2)
        unfollow = driver.find_element(By.XPATH,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div/span')
        
        unfollow.click()
        count+=1
        print('unfollowed {}'.format(person))
    except:
        pass

    # stop after 10 persons have been unfollowed
    if count == 10:
        break 
   
