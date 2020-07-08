import selenium
from selenium import webdriver
import time
import multiprocessing as mp

driver = selenium.webdriver.Firefox()
driver.get("http://researchpark.illinois.edu/tenant-directory/")
while True:
    names = driver.find_elements_by_class_name('med')
    numbers = driver.find_elements_by_class_name('category-news')
    # [print(number.text) for number in numbers]
    emails = driver.find_elements_by_class_name('company-name')
    # [print(email.text) for email in emails]
    assert len(names) == len(numbers) and len(numbers) == len(emails)
    for name, number, email in zip(names, numbers, emails):
        print(" ".join((name.text, number.text, email.text)))
    # next_button = driver.find_element_by_class_name('next page-numbers')
    try:
        next_button = driver.find_element_by_link_text('Next')
        next_button.click()
    except selenium.common.exceptions.NoSuchElementException:
        break