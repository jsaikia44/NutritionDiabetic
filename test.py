import cv2
import pickle
import picamera
import numpy as np



camera = picamera.PiCamera()
camera.capture("image.jpg")
im_test=cv2.imread("image.jpg")
im_test_blue=im_test[:,:,2]
img1=cv2.resize(im_test_blue, (200,200))
imag1=np.expand_dims(img1, axis=2)
X_test=img1
import keras

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


filepath ="/Desktop/model/weights.h5"
model.load_weights(filepath)

pred =model.predict(X_test)
print(pred)