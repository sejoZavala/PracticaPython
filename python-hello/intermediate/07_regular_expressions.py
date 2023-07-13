### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I )
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

# print(re.match("Expresiones Regulares", my_string))

# search
print('******Search******')
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall
print('******Find All******')

findall = re.findall("lección", my_string, re.I)
print(findall)

# split
print('******Split******')

print(re.split(":", my_string))


# sub
print('******Sub******')

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))




### Regular Expressions Patterns ###
# Para aprender y validar expresiones regulares: https://regex101.com
print('*********************************')
print('*********************************')
print('******Expresiones Regulares******')

pattern = r"[lLrR]ección"
print(re.findall(pattern, my_string))


pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))




pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

start, end = re.search(pattern, my_string).span()
print(my_string[start:end])


print('***********************')
pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
pattern = r"\b[^\W\d]+\b"
print(re.findall(pattern, my_string,flags=re.I | re.U ))

print('***********************')

email = "jjmzava@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "jjmzava@gmail.com;otroCorreo@gmail.com;otroCorreo#gmail.com"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+"
print(re.findall(pattern, email))


email = "jjmzava@gmail.com;     mail2@mail.com.mx;      mail3@mail.org;     mail4@mail.mx;      mail555@mail.mex"
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(?:com|org|mex)(?![\w.-])"
print(re.findall(pattern, email))

exit()
