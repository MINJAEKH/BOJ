#수학 #정수론 #유클리드 호제법
num1, num2 = map(int, input().split())
n, m = max(num1, num2), min(num1, num2)

def GCD(n : int, m :int) : # n > m
    while True :
        r = n % m
        if r != 0 :
            n = m; m = r
        elif r == 0 :
            break
    return m

def LCM (n, m, gcd) :
    return n*m // gcd

gcd = GCD(n,m)
lcm = LCM (n, m, gcd)

print(gcd)
print(lcm)