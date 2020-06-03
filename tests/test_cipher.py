import pytest
from caesar_cipher.caesar_cipher import (
    encrypt,
    decrypt,
    break_code
)

@pytest.mark.parametrize(
    'element, key, expected',
    [
        ('abc', 1, 'bcd'),
        ('abc', 27, 'bcd'),
        ('abcde', 1, 'bcdef'),
        ('abc123de', 1, 'bcd123ef'),
        ('Zz', 1, 'Aa'),
        ('123 test me', 1, '123 uftu nf'),
        ('I want to this to be encoded with a shift of over 9000', 9001, 'N bfsy yt ymnx yt gj jshtiji bnym f xmnky tk tajw 9000')
    ],
)

def test_all_encryptions(element, key, expected):
    encrypted = encrypt(element, key)
    assert encrypted == expected
    decrypted = decrypt(encrypted, key)
    assert decrypted == element

@pytest.mark.parametrize(
    "element, key",
    [
        ('It was the best of times, it was the worst of times.', 3),
        ('It was a cold sunny day in May, what will we do', 10),
        ('How are you doing today with this lab?', 17),
        ('What do you think this code will be?', 99)
    ],
)

def test_all_breaks(element, key):
    encrypted = encrypt(element, key)
    broken = break_code(encrypted)
    assert broken == element

