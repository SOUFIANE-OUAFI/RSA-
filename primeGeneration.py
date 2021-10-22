#!/usr/bin/python3

import random # random generation library
import subprocess

def random_prime(size): # size = number of digits of the prime number
	p = random_number(size)
	while(not is_prime(p)):
		p = random_number(size)
	return p


def random_number(size): # size = number of digits of the prime number
	nbr = ""
	random.seed()
	for i in range(size - 1, -1, -1):
		if(i == size - 1):
			nbr += random.choice('123456789')
		elif(i == 0):
			nbr += random.choice('1379')
		else:
			nbr += random.choice('0123456789')
	return int(nbr)

# testing numbers are prime or not
def is_prime(p):
	r = subprocess.run("openssl prime " + str(p), shell = True, stdout=subprocess.PIPE)
	if("is prime" in r.stdout.decode("UTF-8")):
		return 1
	return 0
