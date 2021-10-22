import socket

from rsa import generate_keypair , is_prime ,encrypt ,decrypt
from primeGeneration	import *
import random
import sys

#hote = "localhost"
#port = 12800

###############

def generate_Keys():
    p = 2
    q = 4
    while(not (is_prime(p) and is_prime(q) and p != q)):
        p = int(input("Enter first prim number (3,5,7,13,17,...) : ")) #random_prime(PRIME_SIZE_P)
        q = int(input("Enter second prim number  : ")) #random_prime(MIN_PRIME_SIZE_Q)

    return generate_keypair(p, q)


#----Now comes the sockets part----
HOST = input('Enter host "127.0.0.1 by default": ')
PORT = input('Enter port "8790 by default": ')

if not PORT:
    PORT = 8790
else:
    PORT = int(PORT)

BUFSIZ = 1024 # Buffer size set to handle the exchange chat messages
ADDR = (HOST, PORT)

# generating RSA key pair :
public, private  = generate_Keys()
print("Your public key is ", public, " and your private key is ", private)
##############


connexion_avec_serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexion_avec_serveur.connect((HOST, PORT))
print("Connexion établie avec le serveur sur le port{}".format(PORT))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
	msg_a_envoyer = input("> ")
	# Peut planter si vous tapez des caractères spéciaux
	msg_a_envoyer = msg_a_envoyer.encode("utf8")
	# On envoie le message
	connexion_avec_serveur.send(msg_a_envoyer)
	msg_recu = connexion_avec_serveur.recv(1024)
	print(msg_recu.decode("utf8")) # Là encore, peut planter s'il y a des
	#accents
print("Fermeture de la connexion")
connexion_avec_serveur.close()
