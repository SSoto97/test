#Jercicios de practica
#Como contar cuantas letras o caracteres hay en una palabra
s = "Hoy fui a buscar trabajo por el centro!"
c = "u"
if c in s:
    print("La letra {} esta {} veces en la oracion.".format(c, s.count(c)))


#Hacer un programa que te indica cuando el nuemro es par o impar haciendo uso del operador ternario
n = float(input("Introduce un numero: "))
m = print("El numero es par") if n % 2 == 0 else print("El numero es inpar") 