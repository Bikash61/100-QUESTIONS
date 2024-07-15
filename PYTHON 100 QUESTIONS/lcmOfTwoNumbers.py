def lcm(a,b):
    def gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    return abs(a*b)//gcd(a,b)
print(lcm(18,30))

        