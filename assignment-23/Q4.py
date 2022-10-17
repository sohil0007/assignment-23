def square(n):
    a=1
    while n:
        b=a**2
        yield(b)
        a=a+1
        n-=1

for e in square(int(input("Enter a Number:"))):
    print(e,end=' ') 