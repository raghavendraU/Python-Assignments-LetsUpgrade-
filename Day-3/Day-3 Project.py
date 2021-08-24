#Day-3 Assignment
import random
import string
id =''
characters_list = list(string.ascii_letters + string.digits)
for i in range(6):
  id +=random.choice(characters_list)
print(id)
