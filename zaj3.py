import random
import string

print("\nChar generator")
def random_char(string_length):
    for i in range(string_length):
        print(random.choice(string.ascii_lowercase))
    
random_char(4)
print("\nString generator")
def string_generator(size, stringChain):
   return ''.join(random.choice(stringChain) for _ in range(size))

print(string_generator(10, string.ascii_lowercase))

