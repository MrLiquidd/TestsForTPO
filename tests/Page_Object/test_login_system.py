from LocalHostPages import Imitation


def testing(browser):
    localhost = Imitation(browser)
    localhost.go_to_site()
    localhost.click_on_enter_login_btn()
    localhost.enter_login('12')
    localhost.enter_password('12345678')
    localhost.click_on_login_btn()

