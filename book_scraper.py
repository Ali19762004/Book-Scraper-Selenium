from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
driver=webdriver.Chrome()
products=[]

driver.get(f'https://books.toscrape.com/')
while True:
    
    
    books=driver.find_elements(By.TAG_NAME,'article')
    for book in books:
        product_name=book.find_element(By.CSS_SELECTOR,'h3 a').get_attribute('title')
        product_price=book.find_element(By.CSS_SELECTOR,'.price_color').text
        product_img=book.find_element(By.TAG_NAME,'img').get_attribute('src')
        products.append([product_name,product_price,product_img])
        
    try:
        next_page_link = driver.find_element(By.CSS_SELECTOR, '.next a').get_attribute('href')
        driver.get(next_page_link)
    except:
        print("خلصنا كل الصفحات بنجاح!")
        break
with open('quotes2.csv','w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow(['name','price','img link'])
    writer.writerows(products)
print("File is created successfully with ALL quotes!")



