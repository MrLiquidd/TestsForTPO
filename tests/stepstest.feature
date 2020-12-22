Feature: smoke test #1, testing login and registration

  Scenario: testing Login
    Given open website "http://127.0.0.1:8000/"
    When press button with text "Вход"
    When type to input with name "userName" text: "12"
    When type to input with name "password" text: "12345678"
    When press element with value "Войти"

  Scenario: testing Registration
    Given open website "http://127.0.0.1:8000/"
    When press button with text "Регистрация"
    When type to input all inputs
    When press element with value "Create Account"