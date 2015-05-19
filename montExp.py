import random

def monPro(a, b):
	t = a * b
	temp = (t * _n) % r
	u = (t + (temp * n))/r
	if u > n:
		return u-n, True
	else:
		return u, False

def monExp(m, e, n):
	global stepTrue, stepFalse 
	result = []
	_m = (m * r) % n
	_c = (1 * r) % n
	temp = False
	signif = 1
	for i in e:
		print i
		_c, temp = monPro(_c,_c)
		result.append(temp)
		#if signif == 1:
			#if i == "1": 
		if i == "1":
			_c, temp = monPro(_c, _m)
			print "asdfasdf"
			result.append(temp)
			#print True
			#result.append(True)
		#else:
			#print False
			#result.append(False)
		signif += 1
	c, temp= monPro(_c, 1)
	result.append(temp)
	result.append(c)
	return result



def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


#print _r, _n
def generateSign():
	counter = 0
	
	rsa = []
	mlist = []

	
	#print gcd
	
	while counter<100:
		m = random.randint(100,100000)
		#m = 425
		rsa.append(monExp(m, bin(d), n))
		mlist.append(m)
		#print m
		counter += 1

	for x in range(0, len(rsa)):
		print rsa[x], mlist[x]
#r = 32
n = 3233

#gcd, _r, _n = egcd (r, n)
#
r = 32
#n = 29
d = str(bin(17))[2:]
r = 2**(len(bin(n))-2)
print r, len(d), 2**9, d

gcd, _r, _n = egcd (r, n)
_n = ((r * _r) - 1) / n


#generateSign()