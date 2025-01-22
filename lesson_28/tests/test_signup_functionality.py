import string
from random import choice

name = f'NewTestUser{choice(string.ascii_uppercase)}{choice(string.ascii_lowercase)}'
last_name = f'{name}last'
email = f'{name}@test.com'
password = 'Abracadabra1'

def test_sign_up_on_qauto2_page(driver, open_home_page, open_sign_up_form, input_name,
                                input_last_name, input_email, input_password, repeat_input_password,
                                press_register_button, open_user_profile, check_if_name_present_in_profile):
    open_home_page()
    open_sign_up_form()
    input_name(name)
    input_last_name(last_name)
    input_email(email)
    input_password(password)
    repeat_input_password(password)
    press_register_button()
    open_user_profile()
    assert check_if_name_present_in_profile(name)
