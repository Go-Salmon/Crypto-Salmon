from mono import *
from poly import *
from Zigzag import *
#from AES import *
from DH import *
from cry_RSE import *


def menue_mono():
    print(" [1]- Additive cipher")
    print(" [2]- Multiplicative Cipher")
    print(" [3]- Affine Cipher")
    choice = int(input("Select Algorithm : "))
    if (choice == '1'):
        Add_main()
    elif (choice == '2'):
        Mul_main()
    elif (choice == '3'):
        Aff_main()

def menue_poly():
    print(" [1]- Autokey Cipher")
    print(" [2]- Playfair Cipher")
    print(" [3]- Vigernere Cipher")
    print(" [4]- Hill Cipher")
    choice = int(input("Select Algorithm : "))
    if (choice == '1'):
        main_Auto()
    elif (choice == '2'):
        main_Pla()
    elif (choice == '3'):
        main_Vig()
    elif (choice == '4'):
        main_Hill()

def menue_Sud():
    print(" [1]- Monoalphabetic Ciphers")
    print(" [2]- Polyalphabetic Ciphers")
    choice = int(input("Select Algorithm : "))
    if (choice == '1'):
        menue_mono()
    elif (choice == '2'):
        menue_poly()
    else:
        print("Try again choice:")
        menue_Sud()

def menue_Tra():
    print(" [1]- Rail_fance Cipher")
    choice = int(input("Select Algorithm : "))
    if (choice == '1'):
        main_Zig()
    else:
        print("Try again choice:")
        menue_Tra()

def menue():
    print(" [1]- Substitution Ciphers")
    print(" [2]- Transposition Ciphers")
    print(" [3]- AES Ciphers")
    print(" [4]- RSE Ciphers")
    print(" [5]- Diffie-Hellmen Ciphers")
    choice = int(input("Select Algorithm : "))
    if (choice == '1'):
        menue_Sud()
    elif (choice == '2'):
        menue_Tra()
    #elif (choice == '3'):
    #elif (choice == '4'):
    elif (choice == '5'):
        Diffie_Hellman()
    else:
        print("Try again choice:")
        menue()





