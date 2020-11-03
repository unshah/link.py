import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("https://www.linkedin.com/")

def sign1():
    try:
        sleep(2)
        signin_btn = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
        print("Signin button found")
        signin_btn.click()
    except:
        pass
sign1()

def sign2():
    try:
        sleep(2)
        signin_btn = browser.find_element_by_xpath("/html/body/nav/div/a")
        print("Signin button found")
        signin_btn.click()
    except:
        pass
sign2()

username_input = browser.find_element_by_xpath("/html/body/div/main/div[2]/form/div[1]/input")
password_input = browser.find_element_by_xpath("/html/body/div/main/div[2]/form/div[2]/input")

username_input.send_keys("<emailaddress@gmail.com>")
password_input.send_keys("<password>")

login_btn = browser.find_element_by_xpath("/html/body/div/main/div[2]/form/div[3]/button")
login_btn.click()

print("Signed In Successfully !")
sleep(5)

def close_message():
    try:
        close_message_btn = browser.find_element_by_xpath("/html/body/div[7]/aside/div[1]/header/section[2]/button[2]")
        close_message_btn.click()
        print("Closed messages")
    except:
        pass
close_message()

job_btn =  browser.find_element_by_xpath("/html/body/div[7]/header/div[2]/nav/ul/li[3]/a")
job_btn.click()

#job_input = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/section/section[1]/div/div/div[2]/div[1]/div/div/input")
#job_input.send_keys("Software Engineer")

search_btn = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/section/section[1]/div/div/div[2]/button")
search_btn.click()

print("Job searched successfully !")

sleep(2)

exp_dd = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[2]/form/button")
exp_dd.click()

el = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[2]/form/div/fieldset/div/ul/li[2]/label")
el.click()

apply = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[2]/form/div/fieldset/div/div/button[2]")
apply.click()

jobtype_dd = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[4]/form/button")
jobtype_dd.click()

ft_cb = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[4]/form/div/fieldset/div/ul/li[1]/label")
ft_cb.click()

apply = browser.find_element_by_xpath("/html/body/div[7]/div[3]/div[3]/section/div/div/div[2]/div/div[2]/ul/li[4]/form/div/fieldset/div/div/button[2]")
apply.click()

print("Filtered job successfully !")
