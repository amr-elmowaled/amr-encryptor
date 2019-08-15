import binascii
import zlib

letters = '0ab~c1d<ef!2gh@i3jk#l4m?no$5p>qr6%st`u7^vw"x8y\\&zA,9BC*DE(F.G)HI_JK-LM+N}OP{Q|R/S[TUV]WXYZ\''

letters_equation = lambda index: index+2
binaries_equation = lambda index: index*3-1

def __isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def __letter_convert(letter, value):

    index = letters.find(letter) + value
    while index > len(letters)-1:
        index -= len(letters)-1

    while index < 0:
        index += len(letters)-1
    return letters[index]
        

def __translate(binary, index, value):
    
    start = binary[:3]
    binary = list(binary[3:])
    new_index = index + value    

    while new_index > len(binary)-1:
        new_index -= len(binary)
    code = binary[new_index]
    binary[new_index] = binary[index]
    binary[index] = code
    return start + ''.join(binary)
    
def encrypt(message):
    assert __isEnglish(message)
    encrypted_message = ""
    for index, letter in enumerate(message):
        encrypted_message += __letter_convert(letter, letters_equation(index)) if letter in letters else letter

    encrypted_binary = []
    for index, letter in enumerate(encrypted_message):
        encrypted_binary += [__translate(bin(int(binascii.hexlify(letter), 16)), -((index)%4), binaries_equation(index))]
                
    return to_letters('-'.join(encrypted_binary))


def safe_encrypt(message, percentage=.7):
    """ function return a high percentage of binary layer encryption"""
    assert __isEnglish(message) and percentage <= 1
    while accuracy(encrypt(message)) < percentage:
        message = ' ' + message

    return encrypt(message)

def decrypt(encrypted):
    binaries = [bin(int(binascii.hexlify(i), 16)) for i in encrypted]
    decrypted_binary = []
    encrypted_letters = ""
    decrypted_letters = ""

    for index, binary in enumerate(binaries):
        decrypted_binary += [__translate(binary, -((index)%4), binaries_equation(index))]

    for index, binary in enumerate(decrypted_binary):
        encrypted_letters += binascii.unhexlify('%x' % int(binary, 2))

    for index, letter in enumerate(encrypted_letters):
        decrypted_letters += __letter_convert(letter, -letters_equation(index)) if letter in letters else letter
    return decrypted_letters.strip()

def super_encrypt(message, safe_encryption=True):
    return zlib.compress(safe_encrypt(message) if safe_encryption else encrypt(message))


def super_decrypt(message):
    return decrypt(zlib.decompress(message))


def accuracy(encrypted):
    """ function that checks the total change(effect) done by the binary encrypting layer"""
    encrypted = '-'.join([bin(int(binascii.hexlify(i), 16)) for i in encrypted])
    try:
            spaces = ''
            while encrypted.startswith('0b100000-'):
                spaces += ' '
                encrypted = encrypted[9:]

            encrypted = '0b100000-'*len(spaces)+encrypted

            tested = to_letters(encrypted)
            real = letter_encrypt(spaces + decrypt(to_letters(encrypted)))
            similarity = len(real)-len(tested)
            for i, j in enumerate(real):
                if j == tested[i] and j != ' ':
                    similarity += 1
            return (len(real.strip())-similarity)*1.0/len(real.strip())
    except ZeroDivisionError:
	    raise "equation has high subtracting number which causes index out of bound"
    except:
        return 1


def letter_encrypt(message):
	encrypted_message = ""
	for index, letter in enumerate(message):
		encrypted_message += __letter_convert(letter, letters_equation(index)) if letter in letters else letter

	return encrypted_message

def letter_decrypt(message):
    encrypted_message = ""
    for index, letter in enumerate(message):
    	encrypted_message += __letter_convert(letter, -letters_equation(index)) if letter in letters else letter

    return encrypted_message



def to_letters(encrypted):
    """ this  function shows you what happens when trying to convert binary to text without decrypting the binary """
    text = ""
    c = encrypted.split("-") if "-" in encrypted else [encrypted]
    for i in c:
    	text += binascii.unhexlify('%x' % int(i, 2))
    return text
