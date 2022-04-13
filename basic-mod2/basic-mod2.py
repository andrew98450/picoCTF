import enum
import gmpy2

fd = open("message.txt", "r")
data = fd.readline().strip().split(' ')

print("EncryptText=")
print(data)

for i, value in enumerate(data, 0):
    data[i] = int(value) % 41

print("1st DecryptText=")
print(data)

for i, value in enumerate(data, 0):
    data[i] = gmpy2.invert(data[i], 41)

print("2nd DecryptText=")
print(data)

