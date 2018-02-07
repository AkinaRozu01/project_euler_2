#dictionary 1:Names
dict_names={'Caylene':'Augustin', 'Erys':'Dennis'}
print dict_names
#dictionary 2: Binary
i=1
dict_binary={}
for i in range (9):
    print(str(bin(i)[2:]))
    dict_binary[i]=str(bin(i)[2:])
    i+=1
print dict_binary

#dictionary 3: Movies
movies={'Avengers':'rating', 'Black Panther':'N/A'}
print movies
#dictionary 4: Alphabet
import string
string.ascii_lowercase
alphabet=(string.ascii_lowercase)
x=1
for letter in alphabet:
    print (x,letter)
    x+=1
dictionary_alphabet={}
y=1 
for letter in alphabet:
    print (y,letter)
    dictionary_alphabet[i]=letter
    y+=1
print dictionary_alphabet
#add to list
order=(dict_names, dict_binary, movies, dictionary_alphabet)
print order
