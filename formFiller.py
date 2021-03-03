# Modified from a stackoverflow script found here: https://stackoverflow.com/questions/58753500/i-am-trying-to-fill-out-a-web-form-with-python-using-data-from-excel

from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# using Pandas to read the csv file
# Put the file path in between the " '' "
source_information = pd.read_csv('',header=None,skiprows=[0])


# creating a procedure to fill the form
# Put your specific meeting site in between the quotation marks on line 19
def fulfill_form(fstname,lstname, user_email):
    # setting the URL for BeautifulSoup to operate in
    url = " "
    my_web_form = get(url).content
    soup = BeautifulSoup(my_web_form, 'html.parser')

    # Setting parameters for selenium to work
    driver = webdriver.Chrome()
    driver.get(url)

    # use Chrome Dev Tools to find the names or IDs for the fields in the form
    input_customer_fstname = driver.find_element_by_xpath('//*[@id="registrant.givenName"]')
    input_customer_lstname = driver.find_element_by_xpath('//*[@id="registrant.surname"]')
    input_customer_email = driver.find_element_by_xpath('//*[@id="registrant.email"]')
    submit = driver.find_element_by_xpath('//*[@id="registration.submit.button"]')
    #input the values and hold a bit for the next action
    input_customer_fstname.send_keys(fstname)
    time.sleep(1)
    input_customer_lstname.send_keys(lstname)
    time.sleep(1)
    input_customer_email.send_keys(user_email)
    time.sleep(1)
    submit.click()
    time.sleep(7)


# creating a list to hold any entries should them result in error
failed_attempts = []

# creating a loop to do the procedure and append failed cases to the list
# Using the index of the columns instead of the names - 0,1,2
for i,row in source_information.iterrows():
    try:
        fulfill_form(source_information[0][i],source_information[1][i], source_information[2][i])
    except:
        failed_attempts.append(source_information[1])
        pass

if len(failed_attempts) > 0:
    print("{} cases have failed").format(len(failed_attempts))

print("Procedure concluded")