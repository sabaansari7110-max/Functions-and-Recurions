#function to convert inches to cms

def inch_to_cms(inch):
    return inch * 2.54

n= int(input("enter vales in nches: "))
print(f"the corresponding vale in cms is {inch_to_cms(n)}")