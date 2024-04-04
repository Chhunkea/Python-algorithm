#TODO: Greatest Common Divisor

def gcd(n ,m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
    
n = 1071
m = 1029
print(gcd(n, m))