
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "jose",
                 "Apellido": "Zav", "Edad": 99, 1: "Python"}

my_dict = {
    "Nombre": "Jose",
    "Apellido": "Zav",
    "Edad": 99,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print('11111111111111111')
print(my_dict[1])
print(my_dict["Nombre"])

print("Jose" in my_dict)
print("Apellido" in my_dict)

# Inserción

print('2222222222222222')
my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización
print('3333333333')
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
print(my_dict)

# Eliminación

del my_dict["Calle"]
print(my_dict)


# Otras operaciones
print('4444444444')

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())



print('5555555555555555555555555')
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)



my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))



my_new_dict = dict.fromkeys(my_dict, "defaultValue")
print((my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

exit()
my_values = my_new_dict.values()
print(type(my_values))

print('66666666666666666')


print(my_new_dict.values())
print(list(my_new_dict.values()))
print(dict.fromkeys(list(my_new_dict.values())).keys())

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

print(tuple(my_new_dict))
print(set(my_new_dict))
