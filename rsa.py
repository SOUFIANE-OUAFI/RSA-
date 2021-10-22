# TCP RSA Algorithms function
import  binascii # to utilize binary and ascii values
import random # To generate the random value

def gcd(a, b): # Greatest Common divisor computation Method
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi): # Multiplication inverse method to check the Co-primality 
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while (e > 0):
        temp1 = int(temp_phi/e)
        temp2 = temp_phi - (temp1 * e)
        temp_phi = e
        e = temp2


        x = x2 - (temp1 * x1)
        y = d - (temp1 * y1)

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

'''
Tests to see if a number is prime.
'''

def is_prime(num): # To verify the number is prime or not
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q): # RSA Key pari generation
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext): # RSA encryption method
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
	# Also Each message/plaintext is cut into blocks of 64 characters
    cipher = int(binascii.hexlify(plaintext.encode('utf-8')), 16) 
    
    # Return the array of bytes
    return lpowmod(cipher, e, n)


def decrypt(pk, ciphertext): # RSA decryption method, parameters are public key and encrypted text
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = lpowmod(ciphertext, d, n)
    
    # Return the array of bytes as a message and cut into blocks of 64 characters
    return binascii.unhexlify(hex(plain)[2:].encode('ascii')).decode('utf-8') #''.join(plain)


def egcd(a, b): # Extended Euclidean Algorithm to check the Integers are coprime 
        x, y, u, v = 0, 1, 1, 0
        while(a != 0):
                q, r = b // a, b % a
                m, n = x - u * q, y - v * q
                b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y


def modinv(a, m): # Modular inversion using extended euclidean algorithm
        gcd, x, y = egcd(a, m)
        if(gcd != 1):
                return None
        return x % m


def lpowmod(x, y, n): #Modular inversion (x**y)%n ; x, y, n entiers
        result = 1
        while(y > 0):
                if(y&1 > 0):
                        result = (result * x) % n
                y >>= 1
                x = (x * x) % n
        return result

if __name__ == '__main__': # We can also test RSA algorithm independtly running the below code
    '''
    Detect if the script is being run directly by the user
    '''
    # print("RSA Encrypter/ Decrypter")
    # p = int(input("Enter a prime number (17, 19, 23, etc): "))
    # q = int(input("Enter another prime number (Not one you entered above): "))
    # print( "Generating your public/private keypairs now . . .")
    # public, private = generate_keypair(p, q)
    # print ("Your public key is ", public, " and your private key is ", private)
    # message = raw_input("Enter a message to encrypt with your private key: ")
    # encrypted_msg = encrypt(private, message)
    # print encrypted_msg
    # print "Your encrypted message is: "
    # print ''.join(map(lambda x: str(x), encrypted_msg))
    # print "Decrypting message with public key ", (53, 323), " . . ."
    # print "Your message is:"
    # print decrypt((37, 323), [66L, 116L, 66L, 116L, 66L, 116L, 66L, 66L, 116L, 66L, 116L, 116L, 116L, 116L]
