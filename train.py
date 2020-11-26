import cv2
import picamera
import numpy as np


# we have 1000 images in datasets (1.jpg to 1000.jpg)

import os
name_list = os.listdir('/Desktop/input_files/')

X_train=[]
y_train=[]
for i in range(len(name_list)):
    s=name_list.split(".")
    im=cv2.imread(name_list[i])
    im_blue=im[:,:,2]
    img=cv2.resize(im_blue, (200,200))
    img = np.expand_dims(img, axis = 2)
    X_train.append(img)
    y_train.append(int(s[0]))
    
    
from keras.layers import Dense,Conv2D,Flatten,MaxPooling2D
from keras.models import Sequential
input_shape=(200,200,1)
model=Sequential()
model.add(Conv2D(4,(3,3),activation='relu',input_shape=input_shape))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(16,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(16,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(10,activation="relu"))
model.add(Dense(1,activation="linear"))
print(model.summary())

model.compile(loss="mean_squared_error",optimizer="adam")
X_train=np.array(X_train)
y_train=np.array(y_train)


model.fit(X_train,y_train,batchsize=8,epochs=100,verbose=1)
filepath="/Desktop/model/weights.h5"
model.save_weights(filepath)










