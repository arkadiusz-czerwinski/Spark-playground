user = 'dev'
password = 'dev'
import pymongo
client = pymongo.MongoClient(f'mongodb+srv://{user}:{password}@cluster0.pjvh9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.playground
mycol = db.job_offers
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('https://pl.linkedin.com/jobs')
job_title = "Data Scientist"
localization = "Polska"
print("On page")
job_section = driver.find_element_by_xpath(r'/html/body/main/section[1]/section/div[2]/section[2]/form/section[1]/input')
job_section.send_keys(job_title)
localization_section = driver.find_element_by_xpath(r'/html/body/main/section[1]/section/div[2]/section[2]/form/section[2]/input')
localization_section.clear()
localization_section.send_keys(localization)
driver.find_element_by_xpath(r'/html/body/main/section[1]/section/div[2]/button[2]').click()

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
try:
    iterr = 0
    all_jobs = []
    while(jobs := driver.find_element_by_xpath(f'/html/body/main/div/section[2]/ul/li[{iterr +1}]/a')):
        iterr += 1
        all_jobs.append(jobs)
except: 
    # Zamykanie okienka o plikach cookies
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/section/div/div[2]/button[2]").click()
    print(f'Found {len(all_jobs)} jobs')
    for job in all_jobs:
        job.click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/main/section/div[2]/section[2]/div/section/button[1]").click()
        sleep(3)
        description = driver.find_element_by_xpath(r'/html/body/main/section/div[2]/section[2]/div').text
        found_job_title = driver.find_element_by_xpath("/html/body/main/section/div[2]/section[1]/div[1]/div[1]/a/h2").text
        found_company_name = driver.find_element_by_xpath("/html/body/main/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[1]").text
        found_offer_date = driver.find_element_by_xpath("/html/body/main/section/div[2]/section[1]/div[1]/div[1]/h3[2]/span").text
        found_location = driver.find_element_by_xpath("/html/body/main/section/div[2]/section[1]/div[1]/div[1]/h3[1]/span[2]").text
        data_dict = {"Job title": found_job_title, "Company name": found_company_name, "Offer date": found_offer_date, "Location": found_location, "Description": description, "_id": found_location + " - " + found_company_name + " - " + job_title}
        mycol.insert_one(data_dict)
        print(data_dict)
    pass




sleep(200)
driver.close()

# Tutaj scripting
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
