# Newton-verfahren

n   = 5           # positive number, read intput generally
eps = n * 10**(-10)
q   = 1 # initial approximation

while not(abs(n-q**2)<eps):
    q = (q + n/q)/2
    
print(q)
