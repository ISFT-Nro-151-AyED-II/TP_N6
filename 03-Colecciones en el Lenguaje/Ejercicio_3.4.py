# MARCO PRÁCTICO
# ==============
# 3.4 Creá un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario 
# validar). Tendrás que ir pidiendo contactos hasta que el usuario diga que no quiere insertar más. 
# No se podrán meter nombres repetidos.

# Creamos un diccionario vacío para almacenar los contactos. La clave será el nombre del contacto y el valor 
# será su número de teléfono.
contactos = {}

print("\n===================")
print("GESTOR DE CONTACTOS")
print("===================\n")

while True:
    nombre = input("Ingresá el nombre del contacto (o escribí 'salir' para terminar): ").strip() 
    # El método strip() elimina espacios en blanco al inicio y al final de la cadena, lo que ayuda a evitar 
    # errores por espacios accidentales.
    
    if nombre.lower() == 'salir':
        break
    
    if not nombre:
        print("El nombre no puede estar vacío.")
        continue
        
    if nombre in contactos:
        print("Ese nombre ya existe en la agenda. No se admiten duplicados.")
        continue

    telefono = input(f"Ingresá el teléfono de {nombre}: ").strip()
    contactos[nombre] = telefono
    print("Contacto agregado con éxito.\n")

print("\nLISTA FINAL DE CONTACTOS")
print("========================\n")
# .items() devuelve una vista de tuplas con el formato (clave-valor) del diccionario. 
# El bucle for desempaqueta estas tuplas automáticamente en las variables nom y tel.
for nom, tel in contactos.items():
    print(f"- {nom}: {tel}")