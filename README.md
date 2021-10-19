# SIXTH PRACTICE INTELLIGENT SYSTEMS
# TIME SCHEDULER

<p align="center">
  <img src="https://iforum-sg.c.huawei.com/dddd/latin/images/2021/2/16/38d4d37a-93f7-46e0-8a7b-379f78a46218.gif" alt="Sublime's custom image"/>
</p>

## NAME 📋
* Juan Luis Canedo Villarroel

### DISCLAIMER

### IMPORTANT! HOW TO USE 🔨

## PROBLEM SUBJECT TO CONSTRAINT SATISFACTION (PSSR) ⚙️

### Variables: :atom: 
* {Speaker1, Speaker2, Speaker3, Speaker4,...}

### Domain : :electron:
* {Day1,Day2,Day3,...}
* {Hour1,Hour2,Hour3,...}
* {Area1,Area2,Area3,...}
          

### Variable assignment : :globe_with_meridians:
* Speaker = {Speaker1:Day2:Hour3:Area3, Speaker3:Day2:Hour1:Area1, Speaker2:Day1:Hour2:Area2}

### Factor :
* f1(Speaker1,Speaker2)
* f2(Speaker2,Speaker3)
* f3(Speaker1,Speaker3)

### Weight : :microscope:
* W(x) = f1(Speaker1:Day2:Hour3:Area3,Speaker2:Day1:Hour2:Area2)*f2(Speaker2:Day1:Hour2:Area2,Speaker3:Day2:Hour1:Area1)*f3(Speaker1:Day2:Hour3:Area3, Speaker3:Day2:Hour1:Area1)

## CLASS AND ATTRIBUTES

### Speaker Class

### Speaker attributes :
* Name 
* Area List = Allows to store all areas of a display 
* Nationality = Saves the speaker's nationality allowing to see if he/she is a foreigner or not

### Timer Class

### Timer Attributes
* Days List = This is a list of the days of the speach.
* Schedule List = This is a list of the hours of the speach. 

### Events Class

### Events attributes :
* Speaker List = This is a list of all the exhibitors who will be giving a speach.
* Time List = It is a list of all the schedules (days and times) that the talks will be given.

## DESCRIPTION OF THE PROBLEM

## SOLUTION DESCRIPTION

## EXPERIMENTS :round_pushpin:



## CONCLUSION


## BIBLIOGRAPHY



