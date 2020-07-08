import selenium
from selenium import webdriver
import time
import multiprocessing as mp


url_template = 'https://www.rtp.org/directory-map/?fwp_paged={}'
driver = selenium.webdriver.Firefox()


def scrape_one_page(page_number):
    url = url_template.format(page_number)
    driver.get(url)
    companies = driver.find_elements_by_class_name('result-details')
    for i in range(len(companies)):
        companies[i].click()
        container = driver.find_element_by_class_name("container")
        div1 = "/html/body/div/div/main/div/div/div[2]/div[1]/div[4]/dl/dd[{}]/span".format(1)
        div2 = "/html/body/div/div/main/div/div/div[2]/div[1]/div[4]/dl/dd[{}]/span".format(2)
        print(driver.title + "\n")
        try:
            result = container.find_element_by_xpath(div1)
            print(result.text + "\n")
        except selenium.common.exceptions.NoSuchElementException:
            print("\n")
        try:
            result = container.find_element_by_xpath(div2)
            print(result.text + "\n")
        except selenium.common.exceptions.NoSuchElementException:
            print("\n")
        print("\n")
        driver.back()
        companies = driver.find_elements_by_class_name('result-details')


for k in range(1, 33):
    scrape_one_page(k)
