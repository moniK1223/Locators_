'''
web-element methods : To interact with the web-elements
    * find_element() : To find and interact with the web-elements
        SYNTAX : driver.find_element('locator_name', 'locator_value')

    * find_elements()


locators: We are having 8 locators
    i)      id
    ii)     name
    iii)    class name
    iv)     tag name
    v)      link text
    vi)     partial link text
    vii)    css selector
    viii)   xpath

'''
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)


#-----------------------------------------------------------------------
## id : It is a locator to locate the webelements
## Whenever we are having id attribute, we go for id locator
## SYNTAX : driver.find_element('id', 'id_value')


# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# username = driver.find_element('id', 'user-name')
# print(username)     ## webelement
# username.send_keys('standard_user')
# time.sleep(1)
#
# pwd = driver.find_element('id', 'password')
# print(pwd)          ## webelement
# pwd.send_keys('secret_sauce')
# time.sleep(1)
#
# login_button = driver.find_element('id', 'login-button')
# print(login_button)
# login_button.click()

#----------------------------------------------------------------------------

# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()

#----------------------------------------------------------------------------
## EG2
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('id', 'name').send_keys('Meera')
# driver.find_element('id', 'email').send_keys('meera@gmail.com')
# driver.find_element('id', 'phone').send_keys('9807612345')
# driver.find_element('id', 'textarea').send_keys('Bengaluru')
# driver.find_element('id', 'female').click()
# driver.find_element('id', 'sunday').click()
#
# #---------------------------------------------------------------------------
# ## name : Whenever we are having name attribute we can go for name locator
# ## SYNTAX : driver.find_element('name', 'name_value')
#
# ## EG1
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('name', 'user-name').send_keys('standard_user')
# driver.find_element('name', 'password').send_keys('secret_sauce')
# driver.find_element('name', 'login-button').click()
#
#
# ## EG2
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('name', 'gender').click()
#
# ## Whenever we are having multiple occurances of the same name locator and its value,
# ## driver will always consider the first occurance
#
# #------------------------------------------------------------------------
# ## class name : class attribute is the class name locator
#
# # ## EG1
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('class name', 'ico-register').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-login').click()
#
# ## Eg2
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('class name', 'form-control').send_keys('Ram')
# driver.find_element('class name', 'form-control').send_keys('ram@gmail.com')
#
# ## In the above example, both the name and email will be filled in the name field
# ## Because, whenever we are having multiple occurances of the same class name and its value,
# ## class name is always going to consider the first occurance
#
#
# ## Eg3
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('class name', 'input_error form_input').send_keys('standard_user')
#
# ## NoSuchElementException
# ## we are getting error because the classname value is having space in it.
# ## To overcome this error, we replace the spaces with  dot(.)
#
# ##
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')

#------------------------------------------------------------------------------
## tagname

# path = r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\css_selector_dup.html'
# driver.get(path)
# time.sleep(3)
#
# driver.find_element('tag name', 'input').send_keys('Ram')
# time.sleep(1)
# driver.find_element('tag name', 'input').send_keys('ram@1234')

## Whenever we are having multiple occurances of the tag name, the tag name locator will always consider first occurance

#----------------------------------------------------------------------------------
## link text : The text present between the anchor tag, we call it as link text

##EG1
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('link text', 'Home & Living').click()
#
# # ##Eg2
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('link text', 'Register').click()
# time.sleep(2)
# driver.find_element('link text', 'Log in').click()

## NOTE : Can only consider if the tagname is a. If the tagname is not anchor tag, then we cant use link text locator

#-------------------------------------------------------------------------------------


# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('link text', '''Books
#         ''').click()

## NoSuchElementException. Since we are having unwanted spaces, we are getting error

#---------------------------------------------------------------------------
## partial link text :
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('partial link text', 'Book').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Comput').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Regi').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Log ').click()


# ##eg2
# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element('partial link text', 'Electronics').click()

#-----------------------------------------------------------------------------
## css selector : To locate the web-elements who's attributes are not locators, we go for css selector
## SYNTAX : tagname[attr_name="attr_value"]

## DRAWBACKS
##  1. Indexing is not possible(Whenever we are having multiple matches, css selector will always consider the first occurance)
##  2. Cant locate text using css selector
##  3. backtraversing is not possible


# # ## EG1
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[id="login-button"]').click()
# time.sleep(3)
# driver.find_element('css selector', 'button[id="react-burger-menu-btn"]').click()
# time.sleep(1)
# driver.find_element('css selector', 'a[id="logout_sidebar_link"]').click()
# time.sleep(2)
# driver.close()
#
# #----------------------------------------------------------------------------
# # ## EG2
# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# driver.find_element('css selector', 'a[data-group="home-&-living"]').click()
#
# #----------------------------------------------------------------------------
# ## Eg3
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[class="input_error form_input"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[class="input_error form_input"]').send_keys('secret_sauce')

## In this example, both username and pwd will be filled in the username section itself.

#-----------------------------------------------------------------------------
## ASSIGNMENTS
## 1. Login to https://www.instagram.com/ using css selector
## 2. Go to https://demowebshop.tricentis.com/, click on register and fillup the details using css selector
## 3. Go to https://www.facebook.com/signup, fill the details

#----------------------------------------------------------------------------


# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(1)
# driver.find_element('css selector', 'input[id="gender-male"]').click()
# driver.find_element('css selector', 'input[id="FirstName"]').send_keys('ram')
# driver.find_element('css selector', 'input[id="LastName"]').send_keys('sharma')
# driver.find_element('css selector', 'input[id="Email"]').send_keys('ram@gmail.com')
# driver.find_element('css selector', 'input[id="Password"]').send_keys('ram@12345')
# driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys('ram@12345')


##
# driver.get('https://www.facebook.com/signup')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[type="radio"]').click()
#
# #-------------------------------------------------------------------------------

# driver.get("https://www.facebook.com/")
# time.sleep(3)
#
# driver.find_element("css selector", 'a[data-testid="open-registration-form-button"]').click()
# time.sleep(3)
# driver.find_element("css selector", 'input[placeholder="First name"]').send_keys('Sanghamitra')

#---------------------------------------------------------------------------------
## xpath : To locate the elements uniquely
## Two types
##      * Absolute xpath
##      * Relative xpath


## Absolute :   Starts from the root of html
##              We use / to indicate absolute xpath
##              / represents immediate child

## Relative xpath : Doesnot start from the root.
##              We use // to indicate relative xpath


## Attribute name and attribute_value:
##          SYNTAX : //tagname[@attr_name="attr_value"]     ## @ represents attribute

## text
##          SYNTAX : //tagname[text()="text"]

## contains():
##          SYNTAX : //tagname[contains(text(), "text")]

## Group indexing:
##          SYNTAX : (any xpath)[index_number]

#----------------------------------------------------------------------------------
##Eg1
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Ramya')
# driver.find_element('xpath', 'html/body/input[2]').send_keys('ramya@12345')


# ## Eg2
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')

#----------------------------------------------------------------------------------
## Relative xpath

## EG1
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

## EG2

# driver.get('https://www.instagram.com/')
# time.sleep(3)
#
# driver.find_element('xpath', '//input[@name="username"]').send_keys('meera')
# driver.find_element('xpath', '//input[@aria-label="Password"]').send_keys('meera@12345')

#---------------------------------------------------------------------------
## ASSIGNMENTS
## 1. Go to https://demowebshop.tricentis.com/, click on register and fill the details using xpath
## 2. Go to https://testautomationpractice.blogspot.com/, fill the details


#----------------------------------------------------------------------------
## using text
## SYNTAX : //tagname[text()="text"]
#
## EG1
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Electronics"]').click()

#
# # EG 2
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Register"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Log in"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Shopping cart"]').click()



## EG3
# driver.get('https://www.myntra.com/')
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Home & Living"]').click()

#---------------------------------------------------------------------------------
## Using contains
## contains : If we want to locate the partial portion of the text(any tagname), we go for contains
## SYNTAX : //tagname[contains(text(), "text")]


# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(3)
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()

#--------------------------------------------------------------------------------
## NOTE : Whenever we are having multiple occurances of xpath and if we dont pass any index
## number, by default it will always consider the first occurance

#---------------------------------------------------------------------------------
## Eg
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@class="input_error form_input"])[1]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@class="input_error form_input"])[2]').send_keys('secret_sauce')

#------------------------------------------------------------------------------
## dependent-independent xpath
##      * Identify the dependent and independent element
##      * write the xpath of independent element
##      * Traverse back till we find the common match for both dependent and independent element
##      * Continue writing the xpath for the dependent element


## EG1
# ## wap to click on the checkbox of python
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Python"]/..//input[@name="download"]').click()

#---------------------------------------------------------------------------------
## EG2
## wap to click on windows link in demo.html
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(3)
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

#--------------------------------------------------------------------------------
## EG3
## WAP to click on the release notes of python 3.11.7
# driver.get('https://www.python.org/')
# time.sleep(3)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(3)
# driver.find_element('xpath', '//a[text()="Python 3.11.7"]/../..//a[text()="Release Notes"]').click()

#-------------------------------------------------------------------------------------------
## EG4
## wap to fetch the price of nifty50 from moneycontrol
# driver.get('https://www.moneycontrol.com/')
# time.sleep(5)
# nifty_50 = driver.find_element('xpath', '(//a[text()="Nifty 50"])[2]/../../..//b')      ## webelement
# print(nifty_50.text)


#----------------------------------------------------------------------------------------
## EG5
## wap to fetch the gold price
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(5)
# gold_rate = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(gold_rate.text)

#-----------------------------------------------------------------------------------------
## EG6
## WAP to fetch the price of Hindcopper from tradingview
# driver.get('https://in.tradingview.com/')
# time.sleep(3)
# driver.find_element('xpath', '//span[text()="Search markets here"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="query"]').send_keys('hindustan copper')
# time.sleep(2)
# driver.find_element('xpath', '(//span[text()="HINDCOPPER"])[1]').click()
# time.sleep(6)
# hindcopper_price = driver.find_element('xpath', '//span[text()="HINDCOPPER"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(hindcopper_price.text)

#--------------------------------------------------------------------------------------

# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Python"]/..//input[@name="download"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//td[text()="Java"]/..//input[@name="download"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//td[text()="C#"]/..//input[@name="download"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//td[text()="Perl"]/..//input[@name="download"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//td[text()="JavaScript"]/..//input[@name="download"]').click()


# ##
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(2)
#
# languages_list = ['Python', 'Ruby', 'Java', 'C#', 'Perl', 'JavaScript']
#
# for language in languages_list:
#     driver.find_element('xpath', f'//td[text()="{language}"]/..//input[@name="download"]').click()
#     time.sleep(1)

#------------------------------------------------------------------------------------------
## wap to fetch the  elements present in the footer of demowebshop.tricentis.com
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(3)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)      ## [webele1, webele2, webele3, webele4, webele5, webele6,...]
#
# for ele in footer_elements:
#     print(ele.text)

#------------------------------------------------------------------------------------------
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(3)
#
# elements = driver.find_elements('xpath', '//table[@name="selenium"]//td')
# print(elements)     ## [webele1, webele2, webele3, webele4, webele5, webele6,..]
#
# languages_list = []
# for ele in elements:
#     if len(ele.text) !=0:
#         languages_list.append(ele.text)
#
# print(languages_list)
#
# for language in languages_list:
#     driver.find_element('xpath', f'//td[text()="{language}"]/..//input[@name="download"]').click()
#     time.sleep(1)

#---------------------------------------------------------------------------------------------
## wap to fetch all the popular searches in myntra

# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]//a')
# # print(popular_searches)     ## list of webelements ##[webele1, webele2, webele3, webele4, webele5, webele6,...]
#
# for element in popular_searches:
#     print(element.text)


## NOTE : text is a property, it will give the text if present in the webelement

#-----------------------------------------------------------------------------------------
## ASSIGNMENT :
## 1. Go to myntra, search for adidas, select the shoes. wap to print the name and price of all the shoes
## 2. Go to Zomato, serach for the pizza and print the name and price of each pizza
## 3. Go to https://in.bookmyshow.com/, fetch all the recommended movies
## 4. Go to qspiders.com, click on courses, wap to print all the available courses

#-----------------------------------------------------------------------------------
## wap  to fill the textboxes present in demo.html
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(3)
#
# textboxes = driver.find_elements('xpath', '//input[@name="fname"]')     ## [web1, web2, web3, web4, web5, web6, web7, web8, web9]
# places_list = ['bengaluru', 'pune', 'bhopal', 'chennai', 'dhanbad', 'bliaspur', 'hassan', 'Jharkand', 'Belgavi']
#
# for web_ele, place in zip(textboxes, places_list):
#     web_ele.send_keys(place)

#---------------------------------------------------------------------------------------
# ## wap  to fill the textboxes present in demo.html in reverse order
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\selenium-QCO-SOEPSD-A3-2-4\files\demo.html')
# time.sleep(3)
#
# textboxes = driver.find_elements('xpath', '//input[@name="fname"]')     ## [web1, web2, web3, web4, web5, web6, web7, web8, web9]
# places_list = ['bengaluru', 'pune', 'bhopal', 'chennai', 'dhanbad', 'bliaspur', 'hassan', 'Jharkand', 'Belgavi']
#
# for web_ele, place in zip(textboxes[::-1], places_list):
#     web_ele.send_keys(place)
#
# #-----------------------------------------------------------------------------------------
# ## wap to print all the links present in python.org
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# links_list = driver.find_elements('tag name', 'a')      ## [web1, web2, web3, web4, web5,...]
#
# for link in links_list:
#     print(link.get_attribute('href'))

#-----------------------------------------------------------------------

## NOTE : get_attribute() : This will give the attribute value of the given attribute name
##                          get_attribute(attr_name)

#-------------------------------------------------------------------

# driver.get("https://www.myntra.com/")
# time.sleep(4)
#
# driver.find_element('class name', 'desktop-searchBar').send_keys('Adidas')
# time.sleep(3)
#
# driver.find_element('xpath', '//li[text()="Adidas Shoes"]').click()
# time.sleep(5)
#
# shoes_name = driver.find_elements('xpath', '//div[@class="search-searchProductsContainer row-base"]//h4')
# for shoes in shoes_name[::2]:
#     print(shoes.text)
#
# print('------------------------------------------------------------------------')
# shoes_price = driver.find_elements('xpath', '//div[@class="search-searchProductsContainer row-base"]//div[@class="product-price"]')
# for price in shoes_price:
#     print(price.text)


#_---------------------------------------------------------------------------------------
# driver.get("https://www.myntra.com/")
# time.sleep(4)
#
# driver.find_element('class name', 'desktop-searchBar').send_keys('Adidas')
# time.sleep(3)
#
# driver.find_element('xpath', '//li[text()="Adidas Shoes"]').click()
# time.sleep(5)
#
# shoes_name = driver.find_elements('xpath', '//h4[@class="product-product"]')
# shoe_names_list = []
# for shoes in shoes_name[::2]:
#     shoe_names_list.append(shoes.text)
#
# shoe_prices_list = []
# shoes_price = driver.find_elements('xpath', '//div[@class="product-price"]')
# for price in shoes_price:
#     shoe_prices_list.append(price.text)
#
#
# for shoe, price in zip(shoe_names_list, shoe_prices_list):
#     print(shoe, '-', price)

#----------------------------------------------------------------------------------------


# driver.get('https://www.zomato.com/')
# time.sleep(3)
#
# driver.find_element('xpath', '//input[@class="sc-dYcyhn kAGwjm"]').send_keys('Bengaluru')
# time.sleep(1)
#
# driver.find_element('xpath', '//div[@class="sc-18n4g8v-0 gAhmYY sc-fdJbru grsjAk"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//p[text()="Bengaluru"]').click()

# driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys('pizza')
# time.sleep(2)
#
# driver.find_element('xpath','//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//p[text()="Pizza - Delivery"]').click()
# time.sleep(4)
#
# driver.find_element('xpath', '//h4[text()="Oven Story Pizza - Standout Toppings"]').click()
# time.sleep(3)
#
# pizza_names = driver.find_elements('xpath', '//h4[@class="sc-1s0saks-15 iSmBPS"]')
# pizza_names_list = []
# for pizza in pizza_names:
#     pizza_names_list.append(pizza.text)
#
#
# pizza_prices_list = []
# pizza_prices = driver.find_elements('xpath', '//span[@class="sc-17hyc2s-1 cCiQWA"]')
# for price in pizza_prices:
#     pizza_prices_list.append(price.text)
#
# for ele, ele_price in zip(pizza_names_list ,pizza_prices_list):
#     print(ele, '-', ele_price)

#--------------------------------------------------------------------------------------------

#
# driver.get("https://in.bookmyshow.com/")
# time.sleep(3)
#
# driver.find_element('xpath', '//span[text()="Bengaluru"]').click()
# time.sleep(4)
#
# rec_list = driver.find_elements('xpath', '//div[@class="sc-133848s-2 sc-133848s-12 hxPdAO"]')
# for movie in rec_list:
#     print(movie.text)

# driver.get('https://in.bookmyshow.com')
# time.sleep(2)
# driver.find_element('xpath','//span[text()="Bengaluru"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="See All ›"]').click()
# time.sleep(2)
# movies_list = driver.find_elements('xpath','//div[@class="sc-7o7nez-0 hGuczM"]')
#
# for ele in movies_list:
#     print(ele.text)



# driver.get('https://in.bookmyshow.com/')
# time.sleep(3)
#
# driver.find_element('xpath','//span[text()="Bengaluru"]').click()
# movies = driver.find_elements('xpath','//div[@class="sc-133848s-3 sc-133848s-10 dOuCBq"]')
# recommended_movies_list =[]
#
# for movies_list in movies:
#     recommended_movies_list.append(movies_list.text)
#
# print(recommended_movies_list)


# driver.get('https://in.bookmyshow.com/')
# time.sleep(3)
# driver.find_element('xpath','//span[text()="Bengaluru"]').click()
# movies = driver.find_elements('xpath','//div[@class="sc-133848s-2 sc-133848s-12 hxPdAO"]')
# recommended_movies_list =[]
# for movies_list in movies:
#     recommended_movies_list.append(movies_list.text)
#
# print(recommended_movies_list)
#

#
# driver.get('https://in.bookmyshow.com/')
# time.sleep(3)
#
# driver.find_element('xpath','//span[text()="Bengaluru"]').click()
# time.sleep(3)
# movies_list = driver.find_elements('xpath','//div[@class="sc-7o7nez-0 daKrZU"]')
#
#
# for ele in movies_list:
#     print(ele.text)


# driver.get('https://in.bookmyshow.com/')
# time.sleep(3)
# driver.find_element('xpath', '//input[@placeholder="Search for your city"]').send_keys('bhopal')
# time.sleep(1)
# driver.find_element('xpath', '//li[@class="bwc__sc-1iyhybo-9 fMpEag"]').click()
# time.sleep(1)
# movie_names = driver.find_elements('xpath', '(//div[@class="sc-133848s-3 sc-133848s-10 dOuCBq"])[1]//div[@class="sc-133848s-3 cZuToi"]')
# for movie in movie_names:
#     print(movie.text)













































































































































