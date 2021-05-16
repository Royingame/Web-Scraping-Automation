from selenium import webdriver
import time


source1 = "https://www.flipkart.com/apple-iphone-xr-black-64-gb/p/itm261b2d81215dd?pid=MOBFWQ6BYZBUNUBZ&lid=LSTMOBFWQ6BYZBUNUBZHQ9NPT&marketplace=FLIPKART&q=iphone&store=tyy&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=e970c7d7-f05b-476f-ba70-b09932847d29.MOBFWQ6BYZBUNUBZ.SEARCH&ppt=hp&ppn=homepage&ssid=n4k11hb7m80000001621155556513&qH=0b3f45b266a97d70"
#source2 = "https://www.amazon.in/Apple-iPhone-XR-64GB-Black/dp/B07JWV47JW/ref=sr_1_2?crid=2KIW39JLSZWQL&dchild=1&keywords=iphone+11+xr+64&qid=1621155685&sprefix=iphone+11+XR%2Caps%2C296&sr=8-2"
source3 = "https://www.croma.com/apple-iphone-xr-128gb-rom-3gb-ram-mh7l3hn-a-black-/p/230130"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe',options=CO)
print ("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")

print ("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

#print("Connecting to Amazon")
#wd.get(source2)
#wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
#a_price = wd.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/div[10]/div[12]/div/table/tbody/tr[1]/td[2]/span[1]")
#raw_p = a_price.text
# print (raw_p[2:8])
#print (" ---> Successfully retrieved the price from Amazon \n")
#time.sleep(2)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[3]/div[1]/div/div/div/div[3]/div/ul/li[1]/div[2]/span[1]/span[2]")
raw_c = c_price.text
# print (raw_c[1:7])
print (" ---> Successfully retrieved the price from Croma\n")
time.sleep(2)

# Final display
print ("#------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
#print("  Price available at Amazon is: "+raw_p[2:8])
print("   Price available at Croma is: "+raw_c[0:7])