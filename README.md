#Micromnouse-robot
This repository hosts the code and necessary documentation for the Micromouse robot that can solve any maze using pathfinding algorithms.
A project by Team Micromouse as part of the summer intern projects at IvLabs,VNIT,Nagpur,India.
![image](https://github.com/ChinmayK0607/LabelGen/assets/114411195/57440bf6-aa2b-4cc9-b7ba-28c85f5901e3)

Video of micromouse in action - //demo link, will update later:https://media.discordapp.net/attachments/1116080484754141315/1145729609531396257/IMG_0219.mov
Page for the project:https://www.ivlabs.in/summer-projects.html
Build guide and Code Overview: https://hackmd.io/@l_WDq7lkQq29Pz-KD1JPNA/BJf-U8sph

##How it works
The main algorithm of the maze solving is based on the flood fill algorithm which was devised for the MS paint to bucket fill shapes. The code is run till the set goal is reached. The mouse is completely autonomous and decides the path to be taken based on computation and sensor data. The main algorithm as it is remains in ```floodfill.ino```

The code that is responsible for the movement of the motors and eventually the mouse is in ```motorcontrol_micromouse.ino``` which helps to rotate the rotors to a set distance using encoders and motor drivers. We have used n20 motors as they were small yet efficient enough for our usecase. Here is an overview diagram that can help you understand the structure and interconnection of the micromouse.
![image](https://github.com/ChinmayK0607/LabelGen/assets/114411195/275f04d2-ce57-4bb8-8738-3a6d9264fc21)
Here the main components are the sensors, the arduino nano along with the motor drivers and the motors.

We have used UV sensors, three in number to be specific for the detection of forward,left and right paths. The cell dimension is 16 x 8 for each cell. The UV sensors send the data to nano which in term decides if the distance is greater than or less than threshold. There are four main directions of movement namely North(N),South(S),East(E) and West(W). A short pseudocode for better understanding
``` distance = sensor.value()
if distance < threshold:
    sensor.direction() = 0 // cannot move here
else:
    sensor.direction() = 1
```
Since on each turn, the alignment of the directions of senors can't change, necessary changes in the code have been made to tackle this challenge and the output is given after computation in the terms of Forward(F) , Backward(B) , Right(R) and Left(L).

The arduino nano is the main central unit for communicating between the different hardware components. Motors are controlled using motor drivers which were soldered according to pin diagrams necessary with given specifications. The nano decides when and what distance to move the motors on the basis of sensor data. The movement is controlled with the help of encoders present on the motors and with their specifc pulses per rotation value (512 in this case).

The motors use simple turning and correction algorithms and are able to rectify their alignment to some extent.

##How to build the mouse
The electronics and code breakdown along with pin diagrams, connections and instructions can be found here: https://hackmd.io/@l_WDq7lkQq29Pz-KD1JPNA/BJf-U8sph

##Further communications/Help:
If you have a better optimised code, feel free to raise a PR here and we will review it.
For more exciting projects and papers check out our website:https://www.ivlabs.in

**Happy Building!**

