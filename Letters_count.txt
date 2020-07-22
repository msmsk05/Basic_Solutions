sent = input("Please enter a sentence: ")
mydict={}
for i in sent:
    x = sent.count(i)
    mydict.update({i:x})
print(mydict)