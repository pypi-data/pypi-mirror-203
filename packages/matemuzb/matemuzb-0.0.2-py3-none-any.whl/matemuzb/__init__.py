def fib(n):
	mod=10**9+7
	a= [[0,1],[1,1]]
	r=[[1,0], [0,1]]
	def mult(a,b):
		c=[[0, 0], [0, 0]]
		for i in range (2):
			for j in range(2) :
				for k in range (2):
					c[i][j] =(c[i][j]+a[i][k]*b[k][j]) %mod
		return c
	while n > 0:
		if n%2==1:
			r=mult(r,a)
		n=n//2
		a=mult(a, a)
	return r[1][0]
def tubmi(n):
    if n == 1:return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:return False
    return True
def nchitub(n):
    if n == 1:return 2
    s = 1
    for i in range(3,1000000000000000000000,2):
        if tubmi(i): s +=1
        if s == n:
            return i
    return -1
#python -m setup.py sdist bdist_wheel
#twine upload dist/*