s1 = {1,2,3,4,5,6,7,8,9,10}
it=iter(s1)

i=1
while i<=len(s1):
    print(next(it),end=' ')
    i+=1
