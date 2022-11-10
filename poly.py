alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet, range(len(alphabet))))
letter = dict(zip (range(len(alphabet)), alphabet))

def autokeyencrypt(message,key):
    cipher = ''
    cipher = cipher + letter[((index[message[0]] + index[key[0]]) % 26)]
    for i in range(1, len(message)):
        cipher = cipher + letter[((index[message[i]]+index[message[i-1]]) % 26)]
    return cipher

def autokeydecrypt(message, key):
    plain = ''
    plain = plain + letter[((index[message[0]] - index[key[0]]) %26)]
    for i in range(1, len(message)):
        plain = plain + letter[((index[message[i]] - index[message[i-1]]) % 26)]
    return plain

def main_Atu():
	print("<<<<<<<<<<<<<<<<<<<<<<<<<  Autokey Cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print("[1] Encrypt ")
	print("[2] Decrypt ")
	choice = input("Choice :")
	if (choice == '1'):
		key = str(input("Enter The Number Key : "))
		te = str(input("Enter The Text : "))
		e = autokeyencrypt(te,key)
		print("The CipherText : " + e)
	elif (choice == '2'):
		key = str(input("Enter The Number Key : "))
		te = str(input("Enter The Text : "))
		print("The PlinTxet text : " + autokeydecrypt(te,key))

main_Atu()

		                                      #Playfair Cipher

def doplaintext(plainText):
	for s in range(0,len(plainText)+1,2):
		if s<len(plainText)-1:
			if plainText[s]==plainText[s+1]:
				plainText=plainText[:s+1]+'x'+plainText[s+1:]

	if len(plainText)%2!=0:
		plainText=plainText[:]+'x'
	return  plainText

def key_gen ():
	key_5x5 = [['l','g','d','b','a'],
			   ['q','m','h','e','c'],
			   ['u','r','n','i','f'],
			   ['x','v','s','o','k'],
			   ['z','y','w','t','p']]
	return key_5x5

def encrypt(text):
	message = doplaintext(text)
	k = key_gen()
	message.replace("j","i")
	cipher=''
	for m in range(0, len(message)- 1, 2):
		for i in range(5):
			for j in range(5):
				if message[m] == k[i][j]:
					i1=i
					j1=j
					if message[m+1] == k[i][j]:
						i2=i
						j2=j
	if i1 == i2:
		if j1 != 4:
			cipher = cipher + k[i1][j1 + 1]
		else:
			cipher = cipher + k[i1][0]
		if j2 != 4:
			cipher = cipher + k[i2][j2 + 1]
		else:
			cipher = cipher + k[i2][0]

	if j1 == j2:
		if i1 != 4:
			cipher = cipher + k[i1 + 1][j1]
		else:
			cipher = cipher + k[0][j1]
		if i2 != 4:
			cipher = cipher + k[i2 + 1][j2]
		else:
			cipher = cipher + k[0][j2]
		if i1 != i2 and j1 != j2:
			cipher = cipher + k[i1][j2]
			cipher = cipher + k[i2][j1]

	return cipher

def decrypt(text):
	message = text
	k = key_gen()
	plain=''
	for m in range(0, len(message)- 1, 2):
		for i in range(5):
			for j in range(5):
				if message[m] == k[i][j]:
					i1=i
					j1=j
					if message[m+1] == k[i][j]:
						i2=i
						j2=j

	if i1 == i2:
		if j1 != 0:
			plain = plain + k[i1][j1 - 1]
		else:
			plain = plain + k[i1][4]
		if j2 != 0:
			plain = plain + k[i2][j2 - 1]
		else:
			plain = plain + k[i2][4]
	if j1 == j2:
		if i1 != 0:
			plain = plain + k[i1 - 1][j1]
		else:
			plain = plain + k[4][j1]
		if i2 != 0:
			plain = plain + k[i2 - 1][j2]
		else:
			plain = plain + k[4][j2]
		if i1 != i2 and j1 != j2:
			plain = plain + k[i1][j2]
			plain = plain + k[i2][j1]
	return plain

def main_Pla():

	print("<<<<<<<<<<<<<<<<<<<<<<<<<  Playfair Cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
	print("[1] Encrypt ")
	print("[2] Decrypt ")
	choice = input("Choice :")
	if (choice == '1'):
		te = str(input("Enter The Text : "))
		e = encrypt(te)
		print("The CipherText : " + e)
	elif (choice == '2'):
		te = str(input("Enter The Text : "))
		print("The PlinTxet text : " + decrypt(te))




                                          #Vigenere Cipher

def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return (key)
	else:
		for i in range(len(string) -
					   len(key)):
			key.append(key[i % len(key)])
	return ("".join(key))


def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			 ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return ("".join(cipher_text))

def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			 ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return ("".join(orig_text))


def main_Vig():
		print("<<<<<<<<<<<<<<<<<<<<<<<<<  Vigenere Cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
		print("[1] Encrypt ")
		print("[2] Decrypt ")
		choice = input("Choice :")
		if (choice == '1'):
			ke = str(input("Enter The Number Key : "))
			te = str(input("Enter The Text : "))
			keye = generateKey(te, ke)
			e = cipherText(te, keye)
			print("The CipherText : " + e)
		elif (choice == '2'):
			ke = str(input("Enter The Number Key : "))
			te = str(input("Enter The Text : "))
			ked = generateKey(te, ke)
			print("The PlinTxet text : " + originalText(te, ked))



                                               # Hill Cipher


keyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]


# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1


# Following function encrypts the message
def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
													  messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26


def HillCipher(message, key):
	# Get key matrix from the key string
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65

	# Following function generates
	# the encrypted vector
	encrypt(messageVector)

	# Generate the encrypted text
	# from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	# Finally print the ciphertext
	print("Ciphertext: ", "".join(CipherText))



def main_Hill():
    key = str(input("Enter The Number Key : "))
    message = str(input("Enter The Text : "))
    e = HillCipher(message, key)
    print("The CipherText : " + e)
    print("The PlinTxet text : " + message)  # de_autokey(te, ke))


    print("<<<<<<<<<<<<<<<<<<<<<<<<<  Hill cipher   >>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("[1] Encrypt ")
    print("[2] Decrypt ")
    choice = input("Choice :")
    if (choice == '1'):
    	key = str(input("Enter The Number Key : "))
    	message = str(input("Enter The Text : "))
    	e = HillCipher(message, key)
    	print("The CipherText : " + e)
    elif (choice == '2'):
    	key = str(input("Enter The Number Key : "))
    	te = str(input("Enter The Text : "))
    	print("The PlinTxet text : " +message )
