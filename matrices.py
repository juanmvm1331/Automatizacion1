# ARCHIVO GUIA PARA LA CREACION DE MATRICES 
# AUTOMATIZACION 1

#%% ## ESCALAR
a=1

#%% ## VECTO FILA Y VECTOR COLUMNA
import numpy as np

a=np.array([
        [3,-1,0]
        ])

b=np.array([
        [5],
        [0],
        [15]      
        ])


#%% ## Crear MATRIZ
import numpy as np
a=np.array([
        [3,-1,0],
        [-2,1,1],
        [2,-1,4]
        ])


#%% ## MATRIZ NULA
import numpy as np
a=np.zeros(5)
b=np.zeros((5,5))

#%% ## Matriz UNOS
import numpy as np
a=np.ones(5)
b=np.ones((5,5))

#%% ## MATRIZ IDENTIDAD
import numpy as np
a=np.identity(3)

#%% ## SUMA

import numpy as np
a=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])

b=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])
c=a+b
print (c)

#%% ## RESTA
import numpy as np
a=np.array([
        [10,10,10],
        [10,10,10],
        [10,10,10]
        ])

b=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])
c=a-b
print (c)

#%% ## TRANSPUESTA
import numpy as np
a=np.array([
        [3,-1,0],
        [-2,1,1],
        [2,-1,4]
        ])
b=a.transpose()

#%% ## MULTIPLICACION POR ESCALAR
import numpy as np
b=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])

bb=2*b

#%% 


#%% ## INVERSA
import numpy as np
a=np.array([
        [3,-1,0],
        [-2,1,1],
        [2,-1,4]
        ])

c=np.linalg.inv(a)

#%% ## DETERMINANTE
import numpy as np
a=np.array([
        [3,-1,0],
        [-2,1,1],
        [2,-1,4]
        ])
c=np.linalg.det(a)


#%% Producto punto
import numpy as np
b=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ])
b2=2*np.ones((3,3))

bb=b*b2

c=np.sum(bb)

#%% ## SOLUCIONAR SISTEMA DE ECUACIONES
import numpy as np

a=np.array([
        [3,-1,0],
        [-2,1,1],
        [2,-1,4]
        ])

b=np.array([
        [5],
        [0],
        [15]      
        ])

#c=np.dot(np.linalg.inv(a),b)
c=np.linalg.inv(a)@b
print (c)


#%% Secuencias
a=int(input("Ingrese un lado "))

b=int(input("ingrese otro lado "))

c=int(input("ingrese otro lado "))

vol=(a*b*c)
print (vol)

#%% Condiciones

a=int(input("Ingrese numero A "))

b=int(input("Ingrese numero B "))

if a<b:
    print("B es mayor que A")
    
else:
    print("A es mayor que B")
    

#%% Condicionales 2
nota=float(input("Ingrese nota "))

if nota==5 and nota>=4:
    print("Muy bien")
    
elif nota<4 and nota>3:
    print("bien")
    
elif nota<3 and nota>=0:
    print("perdio")

else:
    print("mal dato")
    
    
    
#%% Ciclos
for i in range(1,20,2):
    if (i%2==0 and i%3==0)or(i%5==0):
        print(f"El numero {i} cumple")
else:
    print(f"ciclo finaliza en {i}")


#%%
import numpy as np
a=np.random.rand(50,8)
#%%
b=a[:,0]
c=a[0,:]
d=np.transpose(c)
r=np.reshape(c,(1,8))
#%%
f=np.shape(a)
w=f[0]*f[1]

for i in range(f[0]):
    for j in range(f[1]):
        print(a[i,j])
    if i*j>50:
        break

#%% Matrices aleatorias
#(b - a) * random_sample() + a
import numpy as np
np.random.seed(0)  #seed es una funcion que permite generar siempre la misma matriz de numeros aletorios
a=np.random.randint(100, size=(200,20))
b=np.random.randint(10,100, size=(200,20))
c = -5 + (5+5)*np.random.rand(10,1)
d= (10-1) * np.random.random((3, 2)) +1

#%% Concatenar matrices y vectores
e=3*a
w=np.concatenate((a,e)) #concatenar filas
x=np.concatenate((a,e),axis=1) #concatenar columnas 

w2=np.vstack((a,e)) #concatenar filas
x2=np.hstack((a,e)) #concatenar columnas 

#%% analizar que pasa si se cambia el cero por un 1
aa=np.mean(a,0)
aaa=np.std(a,0)
aaaa=np.sum(a,0)

#%% Reemplazar valores en matrices RECORDAR que hay muchas opciones
z=a<20
zz=sum(z)
Z=np.copy(a) #crear una nueva matriz igual a la matriz a y esta nueva mtriz será Z
Z[Z<20] = 99999
