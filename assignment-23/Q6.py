def nextprime(num):
    while True:
        num+=1
        for e in range(2,num):
            if num%e==0:
                break
        else:
            return num

def primeproduce(N):
    num,count=1,1
    while count<=N:
        num=nextprime(num)
        yield num
        count+=1

l1=[x for x in primeproduce(int(input("Enter a Number:")))]
print(l1)                        