import re
pattern = '[a-zA-Z0-9]+@[a-z]+.(com/ed/net)'
user_input = input()
if (re.search(pattern,user_input)):
    print('valid input')

else:
    print('invalid input')