from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_Sauce:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://www.saucedemo.com/"
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)

    def test_free_user_password(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        time.sleep(2)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(3)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test sonucu: {testResult}")
        time.sleep(3)

    def test_free_password(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        usernameInput.send_keys("standard_user")
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(3)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test sonucu: {testResult}")
        time.sleep(3)

    def test_locked_user(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        time.sleep(1)
        usernameInput.send_keys("locked_out_user")
        time.sleep(2)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.click()
        time.sleep(1)
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
        errorMesssage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMesssage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test sonucu: {testResult}")
        time.sleep(3)
    def test_free_input_closedBtn(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        time.sleep(1)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        closedBtn =  self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        time.sleep(1)
        closedBtn.click()
        time.sleep(3)

    def test_login(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        time.sleep(1)
        usernameInput.send_keys("standard_user")
        time.sleep(1)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.click()
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        loginBTN = self.driver.find_element(By.ID,"login-button")
        loginBTN.click()
        time.sleep(3)


    def test_products_number(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.click()
        time.sleep(1)
        usernameInput.send_keys("standard_user")
        time.sleep(1)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.click()
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        loginBTN = self.driver.find_element(By.ID,"login-button")
        loginBTN.click()
        time.sleep(2)
        listSauce = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı: {len(listSauce)}")
        time.sleep(2),
       


testClass = Test_Sauce()
#testClass.test_free_user_password()
#testClass.test_free_password()
#testClass.test_locked_user()
#testClass.test_free_input_closedBtn()
#testClass.test_login()
#testClass.test_products_number()