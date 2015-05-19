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
	result = []
	_m = (m * r) % n
	_c = (1 * r) % n
	temp = False
	signif = 1
	for i in e:
		print i
		_c, temp = monPro(_c,_c)
		result.append(temp)
		if i == "1":
			_c, temp = monPro(_c, _m)
		
			result.append(temp)

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



n = 29
d = 101
d = str(bin(d))[2:]
r = 2**(len(bin(n))-2)


gcd, _n, _r = egcd(r, n)
_n = ((r * _r) - 1) / n



print monExp(65, d, n)