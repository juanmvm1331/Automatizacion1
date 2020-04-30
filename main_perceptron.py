#%% Librerias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

#%% Funciones creadas
import preprocesamiento
import gradiente
import graficar_matriz_confusion

#%% Cronstruccion de la base de datos
iris = load_iris()
datos = iris.data
etiquetas=iris.target

xl=datos[0:99,0:2]
yl=etiquetas[0:99]

x=np.array(xl)
y=np.array(yl)
y[y==0] = -1

nombre_clases = iris.target_names[0:2] 

#%% Separacion de los datos y normalizacion
xn=preprocesamiento.normalizar(x)
x_train,y_train,x_val,y_val=preprocesamiento.particion_7030(xn,y)

#%% Gradiente
pesos=gradiente.grad_perc(x_train,y_train,0.001,100)

#%% Clasificacion utilizando el modelo
dim=np.shape(x_val)
unos=np.ones((dim[0],1))
X_val=np.concatenate((unos,x_val),1)   
y_predicha = np.sign(X_val@np.transpose(pesos))

#%% Evaluacion de desempeño del modelo 
con_mat=confusion_matrix(y_val, y_predicha)
tn,fp,fn,tp=confusion_matrix(y_val, y_predicha).ravel()
pre=(tn+tp)/(tn+fp+fn+tp)
sen=tp/(tp+fn)
esp=tn/(tn+fp)
#%% Graficas Recordar que estas solo funcionan para 2D
w0=pesos[0,0]
w1=pesos[0,1]
w2=pesos[0,2]
x1=1
x2=0

y1= -(w0/w2)-((w1/w2)*x1)
y2= -(w0/w2)-((w1/w2)*x2)
X11=np.array([x1,x2])
Y11=np.array([y1,y2])

plt.scatter(x_val[:,0], x_val[:,1],c=y_val)
plt.plot(X11,Y11,'b',linewidth=4)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('IRIS')


y_val[y_val==-1] = 0
y_predicha[y_predicha==-1] = 0
#GRAFICAR MATRIZ de CONFUSION
graficar_matriz_confusion.plot_confusion_matrix(y_val, y_predicha, 
                        classes=nombre_clases,title='Matriz de Confusion')


plt.show()

#%% Mostrar desempeño
print(f"La precision     es del {pre*100} %")
print(f"La sensibilidad  es del {sen*100} %")
print(f"La especificidad es del {esp*100} %")


