import hashlib
  
# initializing string
str_hash = str(input("enter the name: "))
  
# encoding string using encode()
# then sending to md5(),sha256(),sha224()
result1 = hashlib.md5(str_hash.encode())
result2 = hashlib.sha256(str_hash.encode()) 
result3 = hashlib.sha224(str_hash.encode())
 
# printing the equivalent hexadecimal value.
print(result1.hexdigest())
print(result2.hexdigest())
print(result3.hexdigest())
