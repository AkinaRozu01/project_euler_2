import string
string.ascii_lowercase
alphabet=list(string.ascii_lowercase)
i=2 
dictionary_alphabet={}
for letter in alphabet:
    dictionary_alphabet[letter]=i
    i+=2
print dictionary_alphabet


s='the mission of atlanta classical academy is to develop students in mind and character through a classical, content-rich curriculum that emphasizes the principles of virtuous living, traditional learning, and civic responsibility.'
#make the message a list
message=list(s)
print message
#create list for encrypted message
encrypted_message=[]
#redefine via my dictionary
#for letter in message:
#   encrypted_message.append(dictionary_alphabet.get (letter))
#print encrypted_message

#test if value is a letter
#if letter.islpha():

for letter in message:
    if letter.isalpha():
        encrypted_message.append(dictionary_alphabet.get (letter))
print encrypted_message
