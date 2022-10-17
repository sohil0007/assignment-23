def even(n):
    a=2
    while n:
        yield(a)
        a=a+2
        n-=1

for e in even(int(input("Enter a Number:"))):
    print(e,end=' ') 