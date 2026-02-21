#program using functions to convert celsius to fahrenheit

# c/5 = f-32/9  (formula to covert c to f)

#1st method-
def f_to_c(f):
    return 5*(f-32)/9

f= int(input("enter temp in f:"))
print(f_to_c(f))


#2nd method-
def f_to_c(f):
    return 5* (f-32)/9

f= int(input("enter temp in f: "))
c= f_to_c(f)
print(f"{round (c, 2)}*c")