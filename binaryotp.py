plain=input("Enter plain text:")
key=input("Enter key:")
result=''
for i in range(len(plain)):
    if plain[i]==key[i]:
       result=result+'0'
    if plain[i] != key[i]:
        result=result+'1'

print("Plaintext:",plain)
print("Key:", key)
print("Encryption:",result)

cipher='011001'
decrypt=''

for j in range(len(cipher)):
    if cipher[j] == key[j]:
        decrypt = decrypt + '0'
    if cipher[j] != key[j]:
        decrypt = decrypt + '1'

print("Decryption:", decrypt)