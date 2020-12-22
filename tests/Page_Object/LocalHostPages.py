from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class LocalHostLocators:
    # Кнопки входа
    ENTER_LOGIN_BTN = (By.CSS_SELECTOR, 'body > center > div > div > p:nth-child(3) > a')
    ENTER_REG_BTN = (By.CSS_SELECTOR, 'body > center > div > div > p:nth-child(4) > a')

    # Поля входа
    USER_NAME_INPUT_FIELD = (By.CSS_SELECTOR, '#id_username')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, '#id_password')
    # Кнопка логина
    LOGIN_BTN = (By.XPATH, '/html/body/center/div/div/form/p[3]/input')

    # поля регистрации
    USER_NAME_REG_FIELD = (By.CSS_SELECTOR, '#id_username')
    USER_FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#id_first_name')
    MAIL_FIELD = (By.CSS_SELECTOR, '#id_email')
    PASSWORD_REG_FIELD = (By.CSS_SELECTOR, '#id_password')
    PASSWORD2_REG_FIELD = (By.CSS_SELECTOR, '#id_password2')
    # Кнопка регистрции
    REG_BTN = (By.XPATH, '/html/body/center/div/div/form/p[6]/input')


class Imitation(BasePage):

    def click_on_enter_login_btn(self):
        time.sleep(1)
        self.find_element(LocalHostLocators.ENTER_LOGIN_BTN, time=2).click()
        assert self.driver.title == 'Login', 'Ошибка перехода на страницу авторизации'
        time.sleep(1)

    def enter_login(self, login):
        login_field = self.find_element(LocalHostLocators.USER_NAME_INPUT_FIELD)
        login_field.send_keys(login)
        time.sleep(1)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(LocalHostLocators.PASSWORD_INPUT_FIELD)
        password_field.send_keys(password)
        return password_field

    def click_on_login_btn(self):
        time.sleep(1)
        self.find_element(LocalHostLocators.LOGIN_BTN, time=2).click()
        assert self.driver.title == 'Главное меню', 'Ошибка перехода на страницу авторизации'

    def click_on_enter_reg_btn(self):
        time.sleep(1)
        self.find_element(LocalHostLocators.ENTER_REG_BTN, time=2).click()
        assert self.driver.title == 'Регистрация', 'Ошибка перехода на страницу авторизации'
        time.sleep(1)

    def reg_user(self, user):
        user_field = self.find_element(LocalHostLocators.USER_NAME_INPUT_FIELD)
        user_field.send_keys(user)
        time.sleep(1)
        return user_field

    def reg_fname(self, fname):
        fname_field = self.find_element(LocalHostLocators.USER_FIRSTNAME_FIELD)
        fname_field.send_keys(fname)
        time.sleep(1)
        return fname_field

    def reg_mail(self, mail):
        mail_field = self.find_element(LocalHostLocators.MAIL_FIELD)
        mail_field.send_keys(mail)
        time.sleep(1)
        return mail_field

    def reg_pass(self, password):
        pass_field = self.find_element(LocalHostLocators.PASSWORD_REG_FIELD)
        pass_field.send_keys(password)
        time.sleep(1)
        return pass_field

    def reg_pass2(self, password2):
        pass_field = self.find_element(LocalHostLocators.PASSWORD2_REG_FIELD)
        pass_field.send_keys(password2)
        time.sleep(1)
        return pass_field

    def click_on_registr_btn(self):
        time.sleep(1)
        self.find_element(LocalHostLocators.REG_BTN, time=2).click()
        assert self.driver.title == 'Django project', 'Ошибка регистрации'