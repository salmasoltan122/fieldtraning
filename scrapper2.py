import bs4
#from bs4 import BeautifulSoup
import csv
import venv
url=requests.get("https://www.amazon.eg/s?k=%D8%A7%D9%84%D9%83%D8%A7%D9%85%D9%8A%D8%B1%D8%A7%D8%AA&i=warehouse-deals&bbn=27972173031&language=ar_AE&crid=2J4GMHJR39K7&sprefix=%D8%A7%D9%84%D9%83%D8%A7%D9%85%D9%8A%D8%B1%D8%A7%D8%AA%2Cwarehouse-deals%2C172&ref=nb_sb_noss_2")

soup=bs4.BeautifulSoup(url.content,'html.parser')
#soup = (url.text,'lxml')
#products_title=soup.find_all('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
#print(products_title)
products = soup.find_all('div',{'class':'data-asin'})

with open ('products.csv','w',encoding='utf-8', newline='')as file:
  witer=csv.writer(file)
  witer.writerow(['product Name','price'])
  for product in products:
    title=product.find('h2','a-size-mini a-spacing-none a-color-base s-line-clamp-4').text
    price=product.find('span','a-color-base').text

    witer.writerow([ title,price ])

    print("Done")
