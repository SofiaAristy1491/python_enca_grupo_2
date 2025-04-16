# Ejercicio 4: Filtrar Diccionario por Valor
# Dado un diccionario con nombres como clave y edades como valor, retornar 
# un nuevo diccionario solo con los mayores de edad (18 o más).

mi_diccionario={"Walter":70, "Andrea":20, "Dulce":7, "Ivan":34, "David":32}
# nuevo_diccionario={}

# for clave,valor in mi_diccionario.items():
#     if valor>=18:
#         nuevo_diccionario[clave]=valor

# print(nuevo_diccionario)

def clasificar(diccionario):
    nuevo_diccionario={}
    for clave,valor in diccionario.items():
        if valor>=18:
            nuevo_diccionario[clave]=valor
    return nuevo_diccionario

print(clasificar(mi_diccionario))
