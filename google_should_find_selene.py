# Comment
from selene import browser, be, have
from selenium import webdriver

driver_options = webdriver.ChromeOptions()
driver_options.page_load_strategy = 'eager'
browser.config.driver_options = driver_options
browser.open('https://google.com')
browser.config.timeout = 20
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
