from LocalHostPages import Imitation


def testing(browser):
    localhost = Imitation(browser)
    localhost.go_to_site()
    localhost.click_on_enter_reg_btn()
    localhost.reg_user('testuser')
    localhost.reg_fname('username')
    localhost.reg_mail('test@mail.ru')
    localhost.reg_pass('12345678')
    localhost.reg_pass2('12345678')
    localhost.click_on_registr_btn()
