def odd(n):
    a=1
    while n:
        yield(a)
        a=a+2
        n-=1

for e in odd(int(input("Enter a Number:"))):
    print(e,end=' ')        
