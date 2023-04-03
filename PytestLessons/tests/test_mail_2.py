import pytest
@pytest.fixture()
def set_up():
    print("Вход в систему выполнен")
    

def test_sending_mail_3(set_up):
    print("Письмо отправлено")

def test_sending_mail_4(set_up):
    print("Письмо отправлено")

#pytest -s -v d:\Python\avtom_selen_smit\pytestLessons\tests\test_mail.py
#python -m pytest -s -v