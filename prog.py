import string
import random


#length of password
z=int(input('What is the length of your password? '))

#function to generate password containing alphanumeric string and punctuations
def gen(size = 10, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(gen(z))
