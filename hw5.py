
def calculate(a,p,x1,y1,x2,y2):
	m = 0
	if x1 != x2:
		m = ((y2-y1) * modinv(x2-x1,p)) % p
	elif (x1 == x2 and y1 == y2):
		m = ((3 * (x1**2) + a) * modinv(2*y1,p)) % p
	x3 = (m ** 2 - x1 - x2) % p 
	y3 = (m * (x1 - x3) - y1) %p
	print "$(", x3, "," , y3, ")$"
	return x3, y3


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
	if a < 0:
		a=a%m

	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m



print calculate(-3,29,15,12,0,-2)