from selenium import webdriver
from selenium.webdriver.common.by import By

import time

usernameinput = input("Enter your Instagram username: ")
passwordinput = input("Enter your Instagram password: ")

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

time.sleep(2)

button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
button.click()

time.sleep(3)

username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys(usernameinput)

password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys(passwordinput)

login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
login.click()

time.sleep(10)

driver.get("https://www.instagram.com/christoskatsandris/followers/")
input("Scroll down in your browser, until all your followers are loaded. Press ENTER to continue when you're ready.")

followers = driver.find_elements(By.XPATH, "//div[@class=' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")

followers_names = []
followers_that_i_dont_follow_back = []
for follower in followers:
    name = follower.get_attribute("innerHTML")
    if "<" in name:
        followers_names.append(name.split("<")[0])
    else:
        followers_names.append(name)

driver.get("https://www.instagram.com/christoskatsandris/following/")
input("Scroll down in your browser, until all people you're following are loaded. Press ENTER to continue when you're ready.")

print("Analyzing followers. Please wait...")

following = driver.find_elements(By.XPATH, "//div[@class=' _ab8y  _ab94 _ab97 _ab9f _ab9k _ab9p _abcm']")

following_names = []
following_that_they_dont_follow_me_back = []
for user in following:
    name = user.get_attribute("innerHTML")
    if "<" in name:
        following_names.append(name.split("<")[0])
    else:
        following_names.append(name)

driver.quit()

for follower in followers_names:
    if follower not in following_names:
        followers_that_i_dont_follow_back.append(follower)
for user in following_names:
    if user not in followers_names:
        following_that_they_dont_follow_me_back.append(user)

print("I don't follow back:", followers_that_i_dont_follow_back)
print("Don't follow me back:", following_that_they_dont_follow_me_back)

input("Press any key to exit.")