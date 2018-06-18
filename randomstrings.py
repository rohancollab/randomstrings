import random
import string
charsetU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charsetL = 'abcdefghijklmnopqrstuvwxyz'
numeric = '0123456789'

#Alphanumeric (lower case , upper case and special characters)
alpha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits+string.punctuation, k=512))
print("Printing - 512 character Alphanumeric (lower case , upper case and special characters)")
print(alpha)
print(len(alpha))

#All uppercase alphabets
alpha = ''.join(random.choices(string.ascii_uppercase, k=512))
print("Printing - 512 character Alphanumeric (All upper case alphabets)")
print(alpha)
print(len(alpha))

#All lower case alphabets
alpha = ''.join(random.choices(string.ascii_lowercase, k=512))
print("Printing - 512 character Alphanumeric (All lower case alphabets)")
print(alpha)
print(len(alpha))

#Alphanumeric with upper case alphabets
alpha = ''.join(random.choices(string.ascii_uppercase+string.digits, k=512))
print("Printing - 512 character Alphanumeric (upper case alphabets and numeric)")
print(alpha)
print(len(alpha))

#Alphanumeric with lower case alphabets
alpha = ''.join(random.choices(string.ascii_lowercase+string.digits, k=512))
print("Printing - 512 character Alphanumeric (lower case alphabets and numeric)")
print(alpha)
print(len(alpha))

#Alphanumeric with upper and lower case alphabets
alpha = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k=512))
print("Printing - 512 character Alphanumeric (upper and lower case alphabets only)")
print(alpha)
print(len(alpha))
