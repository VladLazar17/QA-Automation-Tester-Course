from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome = webdriver.Chrome()  #initializam Chrome


#------------Selector by ID-----------

chrome.get('https://the-internet.herokuapp.com/login') #Navigam catre un URL
#1

username = chrome.find_element(By.ID,'username')
username.send_keys('tomsmith')

#2

password = chrome.find_element(By.ID,'password')
password.send_keys('SuperSecretPassword!')

#3
chrome.get('https://www.saucedemo.com/') #Navigam catre un URL
user = chrome.find_element(By.ID, 'user-name')
user.send_keys('standard_user')

#------------Selector by LinkText-----------

chrome.get('https://ro.wikipedia.org/wiki/Site_web') #Navigam catre un URL
#1
sleep(2)
chrome.find_element(By.LINK_TEXT, 'engleză').click()
#2
sleep(2)
chrome.find_element(By.LINK_TEXT, 'limbă').click()
#3
sleep(2)
chrome.find_element(By.LINK_TEXT, 'oameni').click()

#------------Selector by Partial LinkText-----------

chrome.get('https://ro.wikipedia.org/wiki/Acalefe') #Navigam catre un URL

#1
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'tentac').click()

#2
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'zoolog').click()

#3
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Moner').click()

# ------------Selector by Partial LinkText-----------

#1
chrome.get('http://the-internet.herokuapp.com/forgot_password')
sleep(2)
chrome.find_element(By.NAME, 'email').send_keys('vlad.lazar17@yahoo.com')

#2
chrome.get('https://magento.softwaretestingboard.com/?ref=hackernoon.com')
sleep(2)
chrome.find_element(By.NAME, 'q').send_keys('Jackets')

#3
chrome.get('https://www.saucedemo.com/?ref=hackernoon.com')
sleep(2)
chrome.find_element(By.NAME, 'login-button').click()

#------------Selector by Tag*-----------

#1
chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')

lista = chrome.find_elements(By.TAG_NAME, 'input')
lista[0].send_keys('vlad.lazar17@yahoo.com')
lista[1].send_keys('parola')
sleep(3)

#2
chrome.get('https://magento.softwaretestingboard.com/?ref=hackernoon.com')

chrome.find_element(By.TAG_NAME, 'input').send_keys('Shirts')
sleep(3)

#3
chrome.get('https://www.saucedemo.com/?ref=hackernoon.com')

lista = chrome.find_elements(By.TAG_NAME, 'input')
lista[0].send_keys('vlad.lazar17@yahoo.com')
lista[1].send_keys('parola')
sleep(3)

#------------Selector by Class Name*-----------

#1
chrome.get('https://the-internet.herokuapp.com/login')

chrome.find_element(By.CLASS_NAME, 'radius').click()

sleep(3)

#2
chrome.get('https://phptravels.org/contact.php')

chrome.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys('Vlad')

sleep(3)

#3
chrome.get('https://phptravels.org/contact.php')

chrome.find_elements(By.CLASS_NAME, 'form-control')[3].send_keys('vlad@gmail.com')

sleep(3)

#------------Selector by CSS-----------

#1 - ID
chrome.get('https://phptravels.org/contact.php')

chrome.find_element(By.CSS_SELECTOR, 'input#inputName').send_keys('Vl')

sleep(2)

#2 - Class

chrome.find_elements(By.CSS_SELECTOR, 'input.form-control')[2].send_keys('ad')

sleep(2)

#3 - atribut = valoare

chrome.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('vlad@gmail.com')

sleep(2)


#------------Selector by Xpath-----------


chrome.get('https://demoqa.com/automation-practice-form')

#1 atribut - valoare
chrome.find_element(By.XPATH, '//input[@id="firstName"]').send_keys('Vlad')

chrome.find_element(By.XPATH, '//input[@id="lastName"]').send_keys('Lazar')

chrome.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys('vlad@gmail.com')


#2 Text element

chrome.find_element(By.XPATH, '//label[text()="Male"]').click()

sleep(1)

chrome.find_element(By.XPATH, '//label[text()="Female"]').click()

sleep(1)

chrome.find_element(By.XPATH, '//label[text()="Other"]').click()

sleep(1)

#3 Text partial


chrome.find_element(By.XPATH, '//label[contains(text(), "Mal")]').click()

sleep(1)

#4 SAU, folosind PIPE |

chrome.find_element(By.XPATH, '//input[@id="userNumber"] | //input[placeholder="Mobile Number"]').send_keys('0744654654')

sleep(1)

#5 cu *

chrome.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(' Radu')

sleep(3)

#6 cu parent::

chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong')

#7 cu fratele anterior sau de dupa (la alegere)

chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong/following-sibling::input').send_keys("QA Automation Tester")
sleep(3)

#8 - o funcție ca și cea de la clasă prin care să poti alege prin parametru cu ce element vreai să interacționez.

chrome.get('https://the-internet.herokuapp.com/dropdown')

def select_an_option(option):
    selected_option = Select(chrome.find_element(By.ID, 'dropdown'))
    selected_option.option(option)

select_an_option("Option 1")

sleep(3)