import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
datos = iris.data
etiquetas=iris.target
xl=datos[0:99,0:2]
x=np.array(xl)
unos=np.ones((99,1))
X=np.concatenate((unos,x),1)

yl=etiquetas[0:99]
Y=np.array(yl)

w0=0.9
w1=-3
w2=2.3
x1=4
x2=7
y1= -(w0/w2)-((w1/w2)*x1)
y2= -(w0/w2)-((w1/w2)*x2)
X11=np.array([x1,x2])
Y11=np.array([y1,y2])

plt.scatter(X[:,1], X[:,2],c=Y)
plt.plot(X11,Y11)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('IRIS')

w=np.array([1,0.7,0.2])
entrada_clasificar=X[0,:]
suma=w@entrada_clasificar

valor1=np.sign(-10)
valor2=np.sign(10)
valor3=np.sign(0)
