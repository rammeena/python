#d.py
#python property explained
"""Implementation of python property decorator"""

from e import Property

class User:


    def __init__(self, name, email):
        self._name = name
        self._email = None

        #Calls descriptor, verify on change and init

        self.email = email

    def set_email(self, email):
        if '@' not in email:
            raise TypeError

        self._email = email

    def get_email(self):
        return self._email

    print("Instanting descriptor")
    email = Property(get_email, set_email)
    print(type(email))
    print(email)




