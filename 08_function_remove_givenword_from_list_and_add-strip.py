#Function to remove a given word from a list and add strip it at the same time.

#1st method-
def rem(l, word):
    n= []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n
    
l= ["harry", "rohan", "shubham" "an"]
print(rem(l, "an"))



#2nd method-
def rem(l, word):
    return [item.strip(word) for item in l if item.strip()!= word]

l= ["harry", "rohan", "shubham" "an"]
print(rem(l, "an"))