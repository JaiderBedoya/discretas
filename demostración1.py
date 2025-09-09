import math
import sympy as sp
from sympy.abc import x, y

domain_x = range(1,100)
domain_y = range(1,10 **10)

def exists_forall(predicate, domain_x, domain_y):
    return any(all(predicate(x, y) for x in domain_x) for y in domain_y)

P = lambda x,y: x < math.log10(y/2)
Q = lambda x,y: x**2 + y >= x

print("∃y∀x (x < log10(y/2)):", exists_forall(P, domain_x, domain_y))
print("∃y∀x (x^2 + y >= x):", exists_forall(Q, domain_x, domain_y))