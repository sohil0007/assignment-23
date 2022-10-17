from math import gcd


def decor_gcd(hfc_func):
    def is_coprime(x,y):
        if gcd(x,y)==1:
            print(x,"and",y,"are coprime")
        else:
            print(x,"and",y,"are not coprime")
        hfc_func(x,y)    
            
    return is_coprime                

@decor_gcd
def hfc(x,y):
    while x%y!=0:
        r = x%y
        x = y
        y = r
    print("H.F.C. is",y)    

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
hfc(num1,num2)