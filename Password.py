# Solicitar la contraseña al usuario
contrasena = input("Ingresa tu contraseña: ")

def verificar_longitud(contrasena):
    # Verifica la longitud de la contraseña
    if len(contrasena) < 8:
        print("Tu contraseña debe tener al menos 8 caracteres")
        return False
    return True

def verificar_mayusculas(contrasena):
    # Verifica si hay al menos una mayúscula
    if not any(c.isupper() for c in contrasena):
        print("Tu contraseña debe contener al menos una letra mayúscula")
        return False
    return True

def verificar_numero(contrasena):
    # Verifica si hay al menos un número
    if not any(c.isdigit() for c in contrasena):
        print("Tu contraseña debe contener al menos un número")
        return False
    return True

# Verificar cada condición
longitud_valida = verificar_longitud(contrasena)
mayuscula_valida = verificar_mayusculas(contrasena)
numero_valido = verificar_numero(contrasena)

# Si todas las condiciones se cumplen, la contraseña es segura
if longitud_valida and mayuscula_valida and numero_valido:
    print("Tu contraseña es segura")
else:
    print("Tu contraseña no es segura")