#Encode String using md5
import hashlib
import binascii

String = input("Enter The String:")
print()
print("Using md5")
print(hashlib.md5(String.encode('UTF-8')).hexdigest())
print()

#Encode String using sha1,sha256,sha512
print("Using sha1")
print(hashlib.sha1(String.encode('UTF-8')).hexdigest())
print()
print("Using sha256")
print(hashlib.sha256(String.encode('UTF-8')).hexdigest())
print()
print("Using sha512")
print(hashlib.sha512(String.encode('UTF-8')).hexdigest())
print()

#Encode String using salting and iteration
print("Using Salting and Itration")
X=hashlib.pbkdf2_hmac('sha512' , b'String' , b'Salting' , 10000)
binascii.hexlify(X)
print(X)