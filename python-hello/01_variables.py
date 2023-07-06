
string_variable = "una variable de tipo cadena o string"
print(string_variable)

int_variable = 5
print(int_variable)
print(type(int_variable))

int_to_str_variable = str(int_variable)
print(int_to_str_variable)
print(type(int_to_str_variable))

bool_variable = False
print(bool_variable)


print(string_variable, int_to_str_variable, bool_variable)
print("Este es el valor de:", bool_variable)


print(len(string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "jose", "zavala", 'sejoZavala', 99
print("Me llamo:", name, surname,". Mi edad es:",
      age, ". Y mi alias es:", alias)

print("Me llamo: {0} {1}. Mi edad es:{2}. Y mi alias es: {3}".format(name,surname,alias,age))

# name = input("Cual es tu nombre? ")
# age = input("que edad edad? ")
# print("Tus Datos ingresados son: Nombre: {0} y tu Edad: {1}".format(name,age))

# ¿Forzamos el tipo?
data: str = 2222
# data = True
# data = 5
# data = 1.2
print(type(data))