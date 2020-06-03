from nltk.corpus import words

word_list = words.words()

def encrypt(element, key):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_element = ''

    for char in element:
        char = str(char)
        if char in ascii_lowercase:
            idx = ascii_lowercase.find(char)
            shift = (idx + key) % len(ascii_lowercase)
            encrypted_element += ascii_lowercase[shift]
        elif char in ascii_uppercase:
            idx = ascii_uppercase.find(char)
            shift = (idx + key) % len(ascii_uppercase)
            encrypted_element += ascii_uppercase[shift]
        else:
            encrypted_element += char
    return encrypted_element

def decrypt(element, key):
    return encrypt(element, -key)

def break_code(element):

    for key in range(26):
        counter = 0
        something = decrypt(element, key)
        something_list = something.split(' ')

        for word in something_list:
            if word in word_list:
                counter += 1
        
        if (counter / len(something_list)) >= 0.5:
            return something
        else:
            continue

