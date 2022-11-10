# additive

def encrypt_Add(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt_Add(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


def hack_crypto_Add(text):
    message =text
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(letter)):
        translated = ''
        for symbol in letter:
            if symbol in letter:
                num = letter.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letter)
                translated = translated = letter[num]
            else:
                translated = translated + symbol
            print('hacking key #%s: %s' % (key, translated))


def Add_main():


    print("<<<<<<<<<<<<<<<<<<<<<<<<<  Addtive cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("[1] Encrypt ")
    print("[2] Decrypt ")
    choice = input("Choice :")
    if (choice == '1'):
        ke = int(input("Enter The Number Key : "))
        te = str(input("Enter The Text : "))
        e = encrypt_Add(te, ke)
        print("The CipherText : " + e)
    elif (choice == '2'):
        ke = int(input("Enter The Number Key : "))
        te = str(input("Enter The Text : "))
        print("The PlinTxet text : " + decrypt_Add(te, ke))
Add_main()

# Multiplicative Cipher
"""
for i in range(0,26):
    for j in range(0,26):
        if(i * j) %26 == 1:
            print(i,j)
"""


def Encrypto_Mul(text, k):
    plain = text
    key = k
    cipher = ''
    for char in plain:
        if char == '':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) * key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) * key - 97) % 26 + 97)
    return cipher


def Decryption_Mul(Cipher, k):

    Cipher = Cipher
    for i in range(26):
        if (k * i) % 26 == 1:
            key = i
            plain = ''
            for char in Cipher:
                if char == '':
                    plain = plain + char
                elif char.isupper():
                    plain = plain + chr((ord(char) * key - 65) % 26 + 65)
                else:
                    plain = plain + chr((ord(char) * key - 97) % 26 + 97)
    return (plain)


def Mul_main():

    print("<<<<<<<<<<<<<<<<<<<<<<<<<  Multiplicative Cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("[1] Encrypt ")
    print("[2] Decrypt ")
    choice = input("Choice :")
    if (choice == '1'):
        ke = int(input('Please enter the number key form the renge{1,3,5,7,9,11,15,17,19,21,23,25} : '))
        te = str(input("Enter The Text : "))
        e = Encrypto_Mul(te, ke)
        print("The CipherText : " + e)
    elif (choice == '2'):
        ke = int(input('Please enter the number key form the renge{1,3,5,7,9,11,15,17,19,21,23,25} : '))
        te = str(input("Enter The Text : "))
        print("The PlinTxet text : " + Decryption_Mul(te, ke))


"""
    Cipher = Multiplicative.Encryption(text, k)
    k = 7
    print("plain: " + Multiplicative.Decryption(Cipher, k))
    cipher = "Annkycognefkw"
    for i in range(26):
        key = i
        plain = ''
        for char in cipher:
            if char == '':
            
            elif char.isupper():
                plain = plain + char((ord(char) * key - 65) % 26 + 65)
            else:
                plain = plain + char((ord(char) * key - 97) % 26 + 97)
        print("key %s # %s " % (key, plain))
"""


                   #affine
# Implementation of Affine Cipher in Python

# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None # modular inverse does not exist
	else:
		return x % m


# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
	'''
	C = (a*P + b) % 26
	'''
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
				+ ord('A')) for t in text.upper().replace(' ', '') ])



def affine_decrypt(cipher, key):
	'''
	P = (a^-1 * (C - b)) % 26
	'''
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
					% 26) + ord('A')) for c in cipher ])


def Aff_main():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<  Affine Cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("[1] Encrypt ")
    print("[2] Decrypt ")
    choice = input("Choice :")
    if (choice == '1'):
        ke = [int(input("Please enter the number key form the renge{1,3,5,7,9,11,15,17,19,21,23,25} : ")),
              int(input("Enter The Number Key2{0-312} : "))]
        te = str(input("Enter The PlainText : "))
        e = affine_encrypt(te, ke)
        print('Encrypted Text: {}'.format(e))
    elif (choice == '2'):
        ke = [int(input("Please enter the number key form the renge{1,3,5,7,9,11,15,17,19,21,23,25} : ")),
              int(input("Enter The Number Key2{0-312} : "))]
        te = str(input("Enter The CipherText : "))
        print('Decrypted Text: {}'.format(affine_decrypt(te, ke)))
