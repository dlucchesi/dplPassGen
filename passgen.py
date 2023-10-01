import random
import string
import sys

def generate_password(length=12):
  # Remove some characters that can generate errors (like single quotes)
  skip_characters = ['\'', '"', '`', '¨', '´']
  myPunctual = ''.join([s for s in string.punctuation if s not in skip_characters])
  # print(myPunctual)
  
  # Define the character set for the password (you can customize this)
  characters = string.ascii_letters + string.digits + myPunctual

  # Generate a random password by selecting characters randomly
  password = ''.join(random.choice(characters) for _ in range(length))

  return password




# Usage example: Generate a 12-character password
if len(sys.argv) > 1:
  if len(sys.argv) == 2:
    password = generate_password(int(sys.argv[1]))
    print(password)
  else:
    print("USAGE: python passgen.py arg1")
    print("\t >>> arg1 = length")
    print("OR: python passgen.py")
    print("\t >>> default length = 12")
else:
  password = generate_password()  
  # print("Generated Password:", password)
  print(password)