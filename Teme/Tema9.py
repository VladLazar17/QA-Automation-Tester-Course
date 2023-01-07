import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

'''Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
●Test 1
- Verifică dacă noul url e corect

● Test 2
- Verifică dacă page title e corect
● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
● Test 4
- Verifică dacă butonul de login este displayed

● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi

● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed

- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login


● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’'''

class Login(unittest.TestCase):
    url = 'https://the-internet.herokuapp.com/'
    driver = webdriver.Chrome()

    def setUp(self):

        self.driver.get(self.url)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        actual = self.driver.current_url

        assert actual == 'https://the-internet.herokuapp.com/login', 'URL-ul nu este acelasi'
        print('Test1 PASSED')

    def test_2(self):
        title = self.driver.title

        assert title == 'The Internet', 'Titlul nu este corect!'
        print('Test2 PASSED')

    def test_3(self):
        element = self.driver.find_element(By.XPATH, '//h2').text

        assert element == 'Login Page', 'Textul nu e corect!'
        print('Test3 PASSED')

    def test_4(self):
        button = self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i ').is_displayed()

        assert button, 'Butonul nu este afisat'
        print('Test4 PASSED')

    def test_5(self):
        link = self.driver.find_element(By.LINK_TEXT, 'Elemental Selenium').get_property('href')

        assert link == 'http://elementalselenium.com/', 'Atributul nu este corect!'
        print('Test5 PASSED')

    def test_6(self):
        self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

        assert self.driver.find_element(By.XPATH, '//*[@id="flash"]').is_displayed(), 'Eroarea nu este afisata!'
        print('Test6 PASSED')

    def test_7(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmithtom')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword')
        self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

        expected = 'Your username is invalid!'
        actual = self.driver.find_element(By.XPATH, '//*[@id="flash"]').text

        self.assertTrue(expected in actual, 'Error message text is incorrect')
        print('Test7 PASSED')

    def test_8(self):
        self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        self.driver.find_element(By.XPATH, '//*[@class="close"]').click()

        assert self.driver.find_element(By.XPATH, '//*[@id="flash"]').is_displayed(), 'Eroarea a disparut!'
        print('Test8 PASSED')

    def test9(self):
        list = self.driver.find_elements(By.XPATH, '//label')

        assert list[0].text == 'Username', 'Textul nu este cel asteptat!'
        assert list[1].text == 'Password', 'Textul nu este cel asteptat!'
        print('Test9 PASSED')

    def test_10(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

        assert 'secure' in self.driver.current_url, 'URL-ul nu contine "Secure"'

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'flash')))

        assert self.driver.find_element(By.XPATH, '//*[@id="flash"]').is_displayed(), 'Elementul nu este afisat!'
        assert 'secure area!' in self.driver.find_element(By.XPATH,
                                                          '//*[@id="flash"]').text, 'Nu contine "secure area!"'
        print('Test10 PASSED')

    def test_11(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        self.driver.find_element(By.XPATH, '//*[@class="button secondary radius"]/i').click()

        assert self.driver.current_url == 'https://the-internet.herokuapp.com/login'
        print('Test11 PASSED')

    def test_12(self):

        t = self.driver.find_element(By.XPATH, '//*[@class="subheader"]').text
        list = t.split()
        # list.remove('SuperSecretPassword!')

        for i in list:
            if self.driver.current_url != 'https://the-internet.herokuapp.com/secure':
                self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
                self.driver.find_element(By.ID, 'password').send_keys(i)
                self.driver.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
            else:
                print('Am gasit parola!')
                break

        assert self.driver.current_url == 'https://the-internet.herokuapp.com/secure', 'Nu ma reusit sa gasesc parola'
        print('Test12 PASSED')