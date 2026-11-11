#eliminar espacios en blanco

favorite_language = 'python'

print(favorite_language)

#eliminar espacios en blanco a la derecha temporalmente .rstrip() 
print(favorite_language.rstrip())

#eliminar espacion en blanco a la derecha permanentemente

#asociar el valor modificado con el nombre de la variable
favorite_language = favorite_language.rstrip()

print(favorite_language)

#eliminar espacio de la izquierda .lstrip()
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

#eliminar espacios de ambos lados .strip 
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)