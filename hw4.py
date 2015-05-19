import math, fractions, random

def fermatsTest(a, n):
	x = fastermod(a, n - 1, n)

	if x != 1:
		return "witness"

	#elif (n % 2 == 1 and x == 1):
	return "liar"



def millerRabin(a, n):
	k, m = decompose(n)
	x = fastermod(a, n - 1, n)
	if x == 1:
		return "liar"
	for j in range (0, k-1):
		if x == -1 % n:
			return "liar"
		else:
			x = fastermod(x, 2, n)
	return "witness"

def decompose(n):
   exponentOfTwo = 0
 
   while n % 2 == 0:
      n = n/2
      exponentOfTwo += 1
 
   return exponentOfTwo, n

def fastermod(factor,power,modulus):
	result = 1;
	while(power > 0):
		if (power % 2 == 1):	
			result = (result*factor) % modulus
			power = power-1

		power = power/2;
		factor = (factor*factor)%modulus
	return result

def runFermat ():
	witness = {}
	liar = {}
	counter = 0
	for n in numbers:
		#fermat(n)
		#x = int (math.sqrt(n))
		for a in range (1, n):
			tempString = fermatsTest(a,n)
			if tempString == "witness" and n not in witness:
				witness[n] = a
				#print a, n, "witness", witness
			elif tempString == "liar" and n not in liar:
				liar[n] = a
				#print a, n, "liar", liar

			if n in liar and n in witness:
				break

	print "liar", liar, "\n\nwitness",  witness


def runMiller ():
	witness = {}
	liar = {}
	counter = 0
	for n in numbers:
		#fermat(n)
		#x = int (math.sqrt(n))
		for a in range (1, n):
			tempString = millerRabin(a,n)
			if tempString == "witness" and n not in witness:
				witness[n] = a
				#print a, n, "witness", witness
			elif tempString == "liar" and n not in liar:
				liar[n] = a
				#print a, n, "liar", liar

			if n in liar and n in witness:
				break

	print "\n\nliar", liar, "\n\nwitness",  witness


numbers =[41041, 62745, 63973, 75361, 101101, 126217, 172081,
188461, 278545, 340561, 449065, 552721, 656601, 658801,
670033, 748657, 838201, 852841, 997633, 1033669, 1082809,
1569457, 1773289, 2100901, 2113921, 2433601, 2455921]


runFermat()
runMiller()

