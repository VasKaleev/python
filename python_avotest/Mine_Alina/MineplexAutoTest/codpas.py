import hashlib

# Вводим и кодируем пароль
base_password = 'Gw1pqh5yxQ'
password_hash = hashlib.md5(bytes(base_password, 'utf-8'))
password_encode = password_hash.hexdigest()

#input_password = input('Введите пароль: ')

# Раскодируем пароль
input_password_hash = hashlib.md5(bytes(base_password, 'utf-8'))
input_password_encode = input_password_hash.hexdigest()

# Проверяем закодированный пароль и раскодировку пароля
if password_encode == input_password_encode:
    print("Пароль закодированый правильный: ",input_password_encode)
else:
    print("Пароль неправильный")



