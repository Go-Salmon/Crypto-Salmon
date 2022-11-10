def Diffie_Hellman():

    P = int(input("Enter The Number Key1 : "))
    G = int(input("Enter The Number Key2: "))
    a = 4
    print('The Private Key a for A is :%d' % (a))
    x = int(pow(G, a, P))
    b = 3
    print('The Private Key b for B is :%d' % (b))

    y = int(pow(G, b, P))
    ka = int(pow(y, a, P))
    kb = int(pow(x, b, P))

    print('Secret key for the A is : %d' % (ka))
    print('Secret Key for the B is : %d' % (kb))

Diffie_Hellman()