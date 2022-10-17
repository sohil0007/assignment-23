def nextprime(num):
    while True:
        num+=1
        for e in range(2,num):
            if num%e==0:
                break
        else:
            return num

def primeproduce():
    num=1
    while True:
        num=nextprime(num)
        yield num

it = primeproduce()
prime_list=[]
while True:
    ans = input("Do you want to print fib number[y/n]")
    if ans=="y":
        x=next(it)
        print(x)
        prime_list.append(x)
    
    else:
        print(prime_list)
        break