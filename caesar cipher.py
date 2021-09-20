Ulist=[]
Llist=[]
letter='A'
l='a'
for i in range(0,26):
   Ulist.append(letter)
   Llist.append(l)
   letter=chr(ord(letter)+1)
   l = chr(ord(l) + 1)
text=input("Enter plain text for encryption:")
k=int(input("Enter key:"))
result=''
for i in text:
   if i.isupper():
       p = Ulist.index(i)
       c = (p+k)%26
       result=result+Ulist[c]
   elif i.islower():
       p = Llist.index(i)
       c = (p + k) % 26
       result = result + Llist[c]
   elif i.isspace():
       result = result + ' '
print("Cipher text:",result)
