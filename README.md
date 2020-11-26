Internet of Things (IoT)-based framework for non-invasive blood glucose monitoring.
The system is based on Raspberry Pi Zero (RPi)
energised with a power bank, using a visible laser beam and a Raspberry Pi Camera, all implemented
in a glove. Data for the non-invasive monitoring is acquired by the RPi Zero taking a set of pictures
of the user fingertip and computing their histograms. Generated data is processed by an artificial
neural network (ANN) implemented on a Flask microservice using the Tensorflow libraries. In
this paper, all measurements were performed in vivo and the obtained data was validated against
laboratory blood tests by means of the mean absolute error (10.37%) and Clarke grid error (90.32%
in zone A). Estimated glucose values can be harvested by an end device such as a smartphone for
monitoring purposes.

Hardware used:
1. Respberry Pie3
2. 5v LASER
3. Picamera V2.0
4. Power supply
