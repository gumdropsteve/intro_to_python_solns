# Challenge 003
def cipher(text, cipher_alphabet, option):
    if option == 'encipher':
        return text.translate(cipher_alphabet)
    elif option == 'decipher':
        reverse = {value: key for key, value in cipher_alphabet.items()}
        return text.translate(reverse)
    else:
        print('please input OPTION as "encipher" or "decipher"')


a_cipher_alphabet = str.maketrans(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
    '0qAw1BeC9rDtEyF8uGi3HoI7pJl4KkL6jMhNgOfPdQsRaSmTnUb5VvWcXxY2zZ')

test_text = 'a 01 test'
print(test_text)
test_encipher = cipher(test_text, a_cipher_alphabet, 'encipher')
print(test_encipher)  # 0 ZV 31i3
test_decipher = cipher('0 ZV 31i3', a_cipher_alphabet, 'decipher')
print(test_decipher)  # test_text