# Inference
##### Udacity Robotics Nanodegree - Term 2 - Project 1

#### Conveyor Inference
![Conveyor Accuracy](https://github.com/chriswernst/Inference-Udacity-RoboticsND-T2-Project1/blob/master/images/75.41_accuracy_conveyor_cernst.png?raw=true)

The conveyor belt project to detect candy boxes is trained using GoogleNet for 30 epochs. A relatively common initial learning rate of 0.01 is chosen, utilizing step down learning rate decay with gamma set to 0.1, and step size equal to 33%. Stochastic Gradient Descent(SGD) is selected as the solver.
The upper bound of accuracy seemed to be limited to ~75%. This seems to be have been caused by a homogenous training set of images. It was observed that much of the training images were very similar. Very minor, and hardly noticeable augmentation had been performed. 
Upon evaluation, inference latency hovered right around 5ms, which is [acceptable](https://youtu.be/FMWCFqxLSvg). 

#### My Inference Project - Plant Classifier

###### Report
A PDF report can be found [here.](https://github.com/chriswernst/Inference-Udacity-RoboticsND-T2-Project1/blob/master/Ernst_2018_Plant_Classification_Computer_Vision.pdf)
###### Model
The models can be found [here.](https://github.com/chriswernst/Inference-Udacity-RoboticsND-T2-Project1/tree/master/models)
###### Video
A [video of my Plant Classifier](https://youtu.be/FMWCFqxLSvg) in action can be found below. 
[![IMAGE ALT TEXT](http://img.youtube.com/vi/FMWCFqxLSvg/0.jpg)](https://youtu.be/FMWCFqxLSvg)


