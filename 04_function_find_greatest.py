#function to find greatest of three numbers 

def greatest(a, b, c):
    if(a>b and a>c):
       return a
    elif(b>a and b>c):
        return b
    else:
        (c>b and c>a)
        return c
    
a= 23
b= 21
c= 45


print(greatest(a, b, c))
