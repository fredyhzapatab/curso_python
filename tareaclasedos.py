#Tarea Clase Numero Dos

print("/*********** MANEJO DE LISTAS ***********/ \n")

#CREA E IMPRIME LISTA 
marcas_autos = ["BMW","MERCEDES BENZ","AUDI","TOYOTA"]
print("Creamos una Lista de Marca de Autos", marcas_autos)

#AGREGAR UNA MARCA A LA LISTA

marcas_autos.append("BYD")
print("Agregamos una marca a la Lista de Marca de Autos", marcas_autos)

#REMOVEMOS UN ELEMENTO DE LA LISTA

marcas_autos.remove("BYD")
print("Removemos una marca a la Lista de Marca de Autos", marcas_autos)

#INSERTAMOS UNA MARCA EN LA POSICION 3 DE LA LISTA 

marcas_autos.insert(2,"BYD")
print("Insertamos una marca a la Lista en la posicion 3 a lista Marca de Autos", marcas_autos)

#TUPLAS

#MUNICIPIOS DE COLOMBIA

municipios = ("GIRARDOT","RICAURTE","NILO","TOCAIMA")
print("\n /*********** CREACION DE TUPLAS ***********/ \n")
print("CREACION DE TUPLAS ",municipios)

#AGREGAR ITEMS A LA TUPLA
municipios = municipios + ("AGUA  DE DIOS","JERUSALEN")
print("AGREGAR ITEMS A LA TUPLA ",municipios)

municipios=list(municipios)
municipios.remove("JERUSALEN")
print("REMOVER ITEMS A LA TUPLA ",municipios)

# METODOS STRING


print("*------------------METODOS STRING------------------*\n")

oracion = "Hola, Aplicamos los metodos string"

print("|              ORIGINAL                 | '",oracion,"'")
oracion=oracion.upper()
print("| METODO UPPER - CONVIERTE A MAYUSCULAS | '", oracion,"'")
oracion=oracion.lower()
print("| METODO LOWER - CONVIERTE A MINUSCULAS | '", oracion,"'")
oracion=oracion.capitalize()
print("| METODO CAPITALIZE - CONVIERTE LA PRIMERA LETRA EN MAYUSCULA | '", oracion,"'")
oracion=oracion.replace("Hola","Adios")
oracion=oracion.replace("aplicamos","Ya Aplicamos")
oracion=oracion.replace("los","todos los")
print("| METODO REPLACE - REMPLAZA CARACTERES EN EL STRING | '", oracion,"'")

#---------APLICACION DE TODOS LOS METODOS PARA LISTAS------------

print("*-------------- APLICACION DE LOS METODOS PARA LISTAS ----------* \n")

print("LISTA MARCAS DE AUTOS ", marcas_autos,"\n")
marcas_autos.append("LAMBORGINI")
print("METODO APPEND ",marcas_autos)
marcas_autos.insert(5,"BUGATTI")
print("METODO INSERT ",marcas_autos)
marcas_autos.remove("BUGATTI")
print("METODO REMOVE ",marcas_autos)
marcas_autos.pop(0)
print("METODO POP ",marcas_autos)
marcas_autos.sort()
print("METODO SORT ",marcas_autos)
print(f"METODO INDEX - EL INDICE #3 ES: {marcas_autos.index("BYD")} ")
print(f"METODO COUNT - HAY {marcas_autos.count("BYD")} BYD")

#************** CREACION DE DICCCIONARIOS ******************/

print("\n '************ CREACION DE DICCIONARIOS ***********' \n")

libros = {
"Titulo:" : "La voragine",
"Autor:"  : "José Eustasio Rivera",
"Editorial":"Cromos",
"año:" : 1994
}

editoriales = {
"Editorial-1:"  : "Planeta",
"Editorial-2:"  : "Norma",
"Editorial-3:"  : "Scribe"
}

print(f"Diccionario Original {libros}")
print(f"Diccionario Adicional {editoriales}")
libros["Genero"]="Novela"
print(f"Agrega Genero {libros} \n")
print("**********AGREGAR LOS METODOS PARA LOS DICCIONARIOS*********\n")
print(f"METODO GET {libros.get("editorial")}")
print(f"METODO KEYS {libros.keys()}")
print(f"METODO ITEMS {libros.items()}")
print(f"METODO VALUES {libros.values()}")
print("METODO COPY")
print(f"diccionario Original \n {libros}")
libros["Pais: "] = "Colombia"
dicc_copy = libros.copy()
print(f"diccionario copia {dicc_copy}")
libros.clear()
print(f"METODO CLEAR {libros} ")
libros.update(dicc_copy)
print(f"METODO UPDATE {libros} \n")
print("********** INSTRUCCION INPUT ********** \n")

nombres = input("Nombres: ")
apellidos = input("Apellidos: ")
correo = input("Correo: ")

nombres = nombres.upper()
apellidos = apellidos.upper()
correo = correo.lower()

print(f"\nBienvenido Señor(a) {nombres} {apellidos} \nSu Correo Registrado es: {correo}")
