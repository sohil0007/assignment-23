def decor_triangle(perimeter_func):
    def validity_triangle(a,b,c):
        if a+b>=c and b+c>=a and c+a>=b:
            print("Triangle is Valid")
            perimeter_func(a,b,c)

        else:
            print("Triangle is Invalid")
    return validity_triangle        

@decor_triangle                    
def perimeter(a,b,c):
    d=a+b+c
    print(d)

a = int(input("Enter lengths of a:")) 
b = int(input("Enter lengths of b:")) 
c = int(input("Enter lengths of c:"))

perimeter(a,b,c)
