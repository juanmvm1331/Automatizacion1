#%% Librerias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

#%% Funciones creadas
import preprocesamiento

#%% Cronstruccion de la base de datos
iris = load_iris()
datos = iris.data
etiquetas=iris.target

xl=datos[0:99,:]
yl=etiquetas[0:99]

x=np.array(xl)
y=np.array(yl)
y[y==0] = -1

#%% Separacion de los datos y normalizacion
xn=preprocesamiento.normalizar(x)
x_train,y_train,x_val,y_val=preprocesamiento.particion_7030(xn,y)

#%% CREANDO MLP
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(activation='tanh',solver='sgd',hidden_layer_sizes=(2,),
                    learning_rate=('constant'),learning_rate_init=60,max_iter=5)
clf.fit(x_train,y_train) 
y_predicha=clf.predict(x_val)
#activacion: IDENTIFY LOGISTIC TANH RELU
#SOLVER:lbfgs sgd adam
#learning_rate= constant,invscaling adaptive


#%% Evaluacion de desempeño del modelo 
con_mat=confusion_matrix(y_val, y_predicha)
tn,fp,fn,tp=confusion_matrix(y_val, y_predicha).ravel()
pre=(tn+tp)/(tn+fp+fn+tp)
sen=tp/(tp+fn)
esp=tn/(tn+fp)


#%% Mostrar desempeño
print(f"La precision     es del {pre*100} %")
print(f"La sensibilidad  es del {sen*100} %")
print(f"La especificidad es del {esp*100} %")
