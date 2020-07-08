sayı = input("please enter a number: ")
liste = list(sayı)
digit = len(sayı)

a = 0
if sayı.isalpha():
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
elif sayı.startswith("-"):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    
elif ("." in liste) or ("," in liste):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

else:
    for i in liste:
        a += int(i) ** digit
        
    if int(sayı) == a:
        print("{} is an Armstrong number".format(int(sayı)))
    else:   
        print("{} is not an Armstrong number".format(int(sayı)))