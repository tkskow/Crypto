

def knownE (r, m, e, n, d, rPrime):
	mStar = m + (r * n) % n
	print mStar
	nStar = n * (r*2)
	print nStar
	sStar = (mStar ** d) % nStar
	print sStar
	s = (sStar) % n
	print s
	return s

def randomD (r, m, phiN, n,d):
	print d, r, phiN
	dStar = d + (r * phiN)
	print dStar
	s = ((m ** dStar) % n)
	print s
	return s


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

p,q,n, phiN,e,d = 97,103,9991,9792,2015,8927
m = 25
r = 2**(len(bin(n))-4)
temp = 2**(len(bin(n))-3) * n
#print temp
rPrime = 185


#knownE(r, m, e, n, d, rPrime)
randomD(r,m,phiN,n,d)
fasit = (m ** d) % n
print fasit