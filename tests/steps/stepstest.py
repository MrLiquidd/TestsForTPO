from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('open website "http://127.0.0.1:8000/"')
def step(context):
    context.browser = webdriver.Chrome(executable_path='./chromedriver.exe')
    context.browser.implicitly_wait(10)
    context.browser.get('http://127.0.0.1:8000/')


@when('press button with text "Вход"')
def step_impl(context):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/center/div/div/p[1]/a'))
    )
    context.browser.find_element_by_xpath('/html/body/center/div/div/p[1]/a').click()
    time.sleep(1)


@when('type to input with name "userName" text: "12"')
def step_impl(context):
    context.browser.find_element_by_css_selector('#id_username')\
        .send_keys("12")


@when('type to input with name "password" text: "12345678"')
def step_impl(context):
    context.browser.find_element_by_css_selector('#id_password')\
        .send_keys("12345678")
    time.sleep(1)


@when('press element with value "Войти"')
def step_impl(context):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/center/div/div/form/p[3]/input'))
    )
    context.browser.find_element_by_xpath('/html/body/center/div/div/form/p[3]/input').click()
    time.sleep(2)


@when('press button with text "Регистрация"')
def step_impl(context):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/center/div/div/p[2]/a'))
    )
    context.browser.find_element_by_xpath('/html/body/center/div/div/p[2]/a').click()
    time.sleep(1)


@when("type to input all inputs")
def step_impl(context):
    context.browser.find_element_by_css_selector('#id_username').send_keys("usertest")
    context.browser.find_element_by_css_selector('#id_first_name').send_keys("username")
    context.browser.find_element_by_css_selector('#id_email').send_keys("test@test.test")
    context.browser.find_element_by_css_selector('#id_password').send_keys("12345678")
    context.browser.find_element_by_css_selector('#id_password2').send_keys("12345678")
    time.sleep(1)


@when('press element with value "Create Account"')
def step_impl(context):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/center/div/div/form/p[6]/input'))
    )
    context.browser.find_element_by_xpath('/html/body/center/div/div/form/p[6]/input').click()
    time.sleep(1)