#%% Recordar que hay dos formas de llamar funciones y que todos los códigos deben estar en la misma carpeta
import funciones_ejemplo

a = funciones_ejemplo.suma(3,5)
print(a)
#%% metodo 2
from funciones_ejemplo import suma

aa = suma(10,6)
print(aa)

#%% o se puede crear una funcion dentro del mismo script y llamarla
def resta(a,b):
    c=a-b
    return (c)

z = resta(20,10)
print(z)