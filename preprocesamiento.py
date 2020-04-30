import numpy as np

#%%
def normalizar(x):
    maximos=np.max(x,0)
    minimos=np.min(x,0)
    dim=np.shape(x)
    xn=np.zeros([dim[0],dim[1]])
    for i in range(dim[1]):
        xn[:,i]=(x[:,i]-minimos[i])/(maximos[i]-minimos[i])
    return (xn)

#%%
def particion_7030(x,y):
    dim=np.shape(x)
    lab=np.random.permutation(dim[0])
    labtr=lab[0:round(dim[0]*0.7)]
    labval=lab[round(dim[0]*0.7):dim[0]+1]
    x_train=x[labtr,:]
    y_train=y[labtr,]
    x_val=x[labval,:]
    y_val=y[labval,]
    return (x_train,y_train,x_val,y_val)


#%%
