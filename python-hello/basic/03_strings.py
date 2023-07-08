### Strings ###

string_one = "Mi String"
string_two = 'Mi otro String'

print(len(string_one))
print(len(string_two))
print(string_one + " " + string_two)

new_line = "Este es un String\ncon salto de línea"
print(new_line)

one_tab = "\tEste es un String con tabulación al inicio"
print(one_tab)

scape_string = "\\tEste es un String \\n escapado"
print(scape_string)


# Formato
name, surname, age = "jose", "zavala", 999
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El area del ciruclo con un radio de %d es: %.2f.' % (radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)

# Desempaqueado
language = "pythonManager"
# a, b, c, d, e, f = language #tienen que existir una variable por cada caracter
# print(a)
# print(e)


#haciendo split a una cadena o array
#el arreglo se inicia en posicion 0

language_slice = language[1:3] #inicia en la posicion 1 y termina en la 3-1
print(language_slice)

language_slice = language[1:] #todo apartir de la primera posicion
print(language_slice)

language_slice = language[-2] #todo apartir de la penultima posicion, se incia con -1 de atras para delante 
print(language_slice)

language_slice = language[1:15:3] # de un rango inicial a final va haciendo saltos
print(language_slice)

language_reverse = language [::-1]
print(language_reverse)



print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo


arr = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(arr)
print(result) 

