# name: str = "happey"

# find: list = list(str(name.find('u')))

# print(find[0])

import bcrypt
import encodings

password = bytes('my password')
# data: str = encodings.normalize_encoding("mypassword")

print(bcrypt.hashpw(password=password, salt=bcrypt.gensalt()))

