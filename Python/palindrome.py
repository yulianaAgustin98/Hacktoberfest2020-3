'''
Checks if user input is a palindrome,
e.g. abba is a palindrome,
it is the same word when reading backwards
'''

text = input("Enter text: ")


text = text.casefold()

# reverse the string
rev_text = reversed(text)

# check if the string is equal to its reverse
if list(text) == list(rev_text):
   print("{} is a palindrome.".format(text))
else:
   print("{} is not a palindrome.".format(text))
