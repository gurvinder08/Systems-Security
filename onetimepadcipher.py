plain='HELLO'
key='XMCKL'

l=[]
letter='A'
result=''
for i in range(0,26):
   l.append(letter)
   letter=chr(ord(letter)+1)

for i in range(len(plain)):
    pi=l.index(plain[i])
    ki=l.index(key[i])
    ci=(pi+ki)%26
    result = result + l[ci]
print("Plain text:",plain)
print("Key:",key)
print("Encrypted text:",result)

decrypt=''
for j in range(len(plain)):
    ci = l.index(result[j])
    ki = l.index(key[j])
    pi = (ci - ki) % 26
    decrypt = decrypt + l[pi]

print("Decrypted text:", decrypt)