import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login(unittest.TestCase):
    URL = 'https://the-internet.herokuapp.com/'
    driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

        form_authentication = self.driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(21) > a')
        form_authentication.click()

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        expected_url = 'https://the-internet.herokuapp.com/login'
        actual_url = self.driver.current_url

        assert actual_url == expected_url, 'Noul URL nu este corect'
        print('Test 1 PASSED')

    def test_2(self):
        expected_title = 'The Internet'
        actual_title = self.driver.title

        assert actual_title == expected_title, 'Titlul paginii nu este corect!'
        print('Test 2 PASSED')

    def test_3(self):
        expected_text_h2 = 'Login Page'
        actual_text_h2 = self.driver.find_element(By.XPATH, '//h2').text

        assert actual_text_h2 == expected_text_h2, 'Textul elementului <h2> nu este corect!'
        print('Test 3 PASSED')

    def test_4(self):
        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')

        assert buton_login.is_displayed(), 'Butonul Login nu este afisat!'
        print('Test 4 PASSED')

    def test_5(self):
        expected_href_link = 'http://elementalselenium.com/'
        actual_href_link = self.driver.find_element(By.CSS_SELECTOR, 'a[target]').get_property('href')

        assert actual_href_link == expected_href_link, 'Atributul href nu este corect!'
        print('Test 5 PASSED')

    def test_6(self):
        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
        buton_login.click()

        pop_eroare = self.driver.find_element(By.CSS_SELECTOR, '#flash')

        assert pop_eroare.is_displayed(), 'Eroarea nu este afisata!'
        print('Test 6 PASSED')

    def test_7(self):
        username = self.driver.find_element(By.CSS_SELECTOR, '#username')
        username.send_keys('tomtom')

        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('parola')

        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
        buton_login.click()

        expected_message = 'Your username is invalid!'
        actual_message = self.driver.find_element(By.CSS_SELECTOR, '#flash').text

        self.assertTrue(expected_message in actual_message, 'Mesajul erorii este incorect!')
        print('Test 7 PASSED')

    def test_8(self):
        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
        buton_login.click()

        buton_x = self.driver.find_element(By.CSS_SELECTOR, '.close')
        buton_x.click()

        pop_eroare = self.driver.find_element(By.CSS_SELECTOR, '#flash')

        sleep(2)

        assert pop_eroare.is_displayed(), 'Eroarea a disparut!'
        # self.assertFalse(pop_eroare.is_displayed(), 'Eroarea a disparut!')
        print('Test 8 PASSED')

    def test_9(self):
        lista_elemente = self.driver.find_elements(By.XPATH, '//label')

        assert lista_elemente[0].text == 'Username', 'Textul nu este corect!'
        assert lista_elemente[1].text == 'Password', 'Textul nu este corect!'
        print('Test 9 PASSED')

    def test_10(self):
        username = self.driver.find_element(By.CSS_SELECTOR, '#username')
        username.send_keys('tomsmith')

        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('SuperSecretPassword!')

        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
        buton_login.click()

        assert '/secure' in self.driver.current_url, 'URL-ul nu contine /secure!'
        element = self.driver.find_element(By.CSS_SELECTOR, '.flash.success')
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))

        assert element.is_displayed(), 'Elementul nu este afisat!'
        assert 'secure area!' in element.text, "Nu contine mesajul 'secure area!'"
        print('Test 10 PASSED')

    def test_11(self):
        username = self.driver.find_element(By.CSS_SELECTOR, '#username')
        username.send_keys('tomsmith')

        password = self.driver.find_element(By.CSS_SELECTOR, '#password')
        password.send_keys('SuperSecretPassword!')

        buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
        buton_login.click()

        buton_logout = self.driver.find_element(By.CSS_SELECTOR, '.button')
        buton_logout.click()

        expected_url = 'https://the-internet.herokuapp.com/login'
        current_url = self.driver.current_url
        assert current_url == expected_url, 'URL-ul nu este corect!'
        print('Test 11 PASSED')

    def test_12(self):
        element = self.driver.find_element(By.CSS_SELECTOR, '.subheader')
        lista_parole = element.text.split()

        for i in range(0, len(lista_parole)):
            if self.driver.current_url != 'https://the-internet.herokuapp.com/secure':
                username = self.driver.find_element(By.CSS_SELECTOR, '#username')
                username.send_keys('tomsmith')
                password = self.driver.find_element(By.CSS_SELECTOR, '#password')
                password.send_keys(lista_parole[i])
                buton_login = self.driver.find_element(By.CSS_SELECTOR, '.radius')
                buton_login.click()
            else:
                print(f'Parola secreta este [{lista_parole[i - 1]}].')
                break

        assert self.driver.current_url == 'https://the-internet.herokuapp.com/secure', 'Nu am reusit sa gasesc parola'
        print('Test 12 PASSED')
