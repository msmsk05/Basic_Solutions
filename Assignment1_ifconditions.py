password = "W@12"
name = "Mehmet"
newname = input("Please enter your name: ").title().strip()
if name == newname :
    print("Hello,", "\033[1m" + name+"\033[0m"+"! The password is:",password)
else:
    print("Hello,", "\033[1m" + newname+"\033[0m"+"!","See you later.")