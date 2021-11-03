# SIXTH PRACTICE INTELLIGENT SYSTEMS
# TIME SCHEDULER

<p align="center">
  <img src="https://cdn.dribbble.com/users/135660/screenshots/1308392/iphone-calendar.gif" alt="Sublime's custom image"/>
</p>

## NAME 📋
* Juan Luis Canedo Villarroel

### DISCLAIMER

### IMPORTANT! HOW TO USE 🔨

* Clonar desde el repositorio principal usando: 

     -git clone (enlace al repositorio)

* Insertar en la terminal de la consola 'python main.py' para iniciar el programa






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


### INTRODUCTION 
On many occasions, problem solving is subject to the various units into which they can be decomposed verifying certain sets of constraints. Everyday problems such as making an appointment with friends, buying a car, or preparing a cooking recipe may depend on many interdependent, and even conflicting, aspects subject to a set of constraints that must be satisfied in order to find a solution to the problem posed.

Historically, the representation and resolution of constraint satisfaction problems (CSP) has generated great expectation among experts in many areas due to its potential for solving large real problems that fall, on many occasions, within what are known as NP problems (those that present a higher computational complexity for their resolution). The first works related to constraint programming date back to the 60s and 70s in the field of Artificial Intelligence, although its techniques have been developed much earlier in different areas of mathematics and with applications to economics, engineering, physics, etc.

The idea of PSR is to represent problems by declaring constraints on the problem area (the space of possible solutions) and consequently finding solutions that satisfy all the constraints. Sometimes, solutions are sought that, in addition, optimize some given criteria.

Problem solving with constraints can be divided into two clearly differentiated branches, where fundamentally different methodologies are applied: the one dealing with problems with finite domains, and the one dealing with problems over infinite domains or more complex domains. 

### SEARCH TREE

<p align="center">
  <img src="http://www.cs.us.es/~fsancho/images/2016-09/psr-tree.png" alt="Sublime's custom image"/>
</p>


The possible combinations of the assignment of values to variables in a PSR generate a search space that can be structured to be viewed as a search tree. In this way, we can then traverse it following the strategy of our choice. The backtracking search, which is the basis on which most PSR algorithms are based, corresponds to the traditional DFS depth-first exploration of the search tree.

## DESCRIPTION OF THE PROBLEM
The Systems Engineering career of the Universidad Catolica Boliviana organizes every year an event that lasts a whole week where it invites national and international speakers to give lectures on topics such as
week-long event where national and international speakers are invited to give talks on interesting and relevant topics in the area of informatics.
topics of interest and relevance in the area of informatics.
The congresses are separated into three areas:
- Computer Security
- Software Engineering
- Artificial Intelligence
Talks in the four areas are held in parallel and students who register for the congress can attend any of them.
conference can attend any of them.
The lectures are held from Monday to Friday, from 9:00 am to 12:00 pm and from 3:00 pm to 6:00 pm.
The following aspects are taken into account when organizing the scheduling of the talks:
- A speaker can give up to 5 talks in the same area but cannot give two talks in a row.
- Two speakers from the same area will not have to be assigned the same time for their talks. Two
speakers who are not from the same area can be assigned the same time for their talks.
- Speakers are asked which day and time they would prefer to give their talks.
- Two international guests should not give a talk at the same time.
- It is not always possible to fill all the schedules because they do not get the required number of speakers.
The committee takes weeks to organize the schedule of the talks so they decided to hire you to write a computer program for them.
to write a computer program that will allow them to automate this work for them.

Your job is to model the problem as a Constraint Satisfaction Problem. Then solve the problem using the BackJumping algorithm or, failing that, the simple Backtrack algorithm and use the heuristics that you have developed.

Use the heuristics that we saw in class such as Most Constrained Value, Less Constrained Value, Forward Checking, Arc-Consistency, and
Checking.

To be able to solve problems subject to the satisfaction of restrictions in order to organize exposure times is due to the fact that the priority is to organize them and not how to get to this organization, and yet all the ways to find a solution to the problem have the same depth in which the order of the actions is not important.





## SOLUTION DESCRIPTION

### DESCRIPTION OF CLASSES IMPLEMENTED FOR THE SOLUTION OF THE PROBLEM
For the solution of the problem of schedules of exhibitors using the algorithms seen in classes three classes were created:
* Day : Allows to store a whole day with its available hours to make a presentation, its attributes are
    -	day=String that stores the name of the day.
    -	hours=List that stores integers of available hours of possible presentations.
* Speaker : Allows to store the data of a speaker including the schedule assignments that will be given, its own attributes are:
    -	name=String that stores the name of the speaker.
    -	area=String that stores the area the speaker belongs to
    -	nationality=String that stores the country of origin of the exhibitor (it is useful to know if he is a foreigner or not)
    -	day=Day list, it is a list of individual days with their names and possible times.
    -	assignment=Bool that lets you know if an exhibitor has already been assigned a time for his talk or not.
    -	domain number=Enter that allows to store the sum of the days and their available hours for each exhibitor.
* Event : Main class in which the algorithms seen in class are implemented, its own attributes are:
    -	speakers=Speaker list 
    -	states_visited=int, number of states visited in the least contrained value algorithm

### DESCRIPTION OF METHODS IMPLEMENTED IN MAIN CLASS
* get_day : Function that returns a string with the name of a specific day according to a specific id that is passed to it, its usefulness is necessary for the search of specific days because they are handled by strings and not integers.
	get_day(self,day_id)
* get_number_day : Function that returns the position of a day in a list (int), a string must be passed, its usefulness is necessary for the search of specific positions of the list of days when a string is passed. 
	get_number_day(self,day)
* get_hours : Function that obtains the hours of a speaker by passing the speaker id and the position of the specific day.
	get_hours(self,speaker_id,day_id)
* delete_hour : Function that deletes the time of a specific day of an exhibitor, passing the specific position of the list of an exhibitor, it uses a small condition that what it does is to verify if the exhibitor has more than one day (class day) available for the realization of an exposition and to eliminate it as list, if it does not have more than one day then it is eliminated as attribute
	delete_hour(self,speaker_id,day_id,hour_id)
* delete_day : Function that deletes a day including all its hours of a speaker, passing an id of the speaker and a day.
	delete_day(self,speaker_id,day_id)
* get_size : Function that returns the size of a list passed to it.
	get_size(self,list)
* set_domain_number : Function that allows to modify the number of domains of a speaker according to the days and hours he is available by checking all the days and hours he is available.
	set_domain_number(self,speaker_id)
* get_domain_number : Function that returns a speaker's attribute of the number of available domains. 
	get_domain_number(self,speaker_id)
* mrv : Heuristic function that chooses a speaker that has the lowest number of domains in its attributes, it uses a list which is iterated until all the speakers are visited and its number of domains is taken from which the lowest one is taken.
	mrv(self)
* neighbors : Function that obtains the neighbors of a specific speaker according to the area to which it belongs returning a list of unassigned neighboring speakers (without an assigned time and day). 
	neighbors(self,area,speaker_id)
* forward_checking : Function that assigns a day and time and removes that time and day from neighbors, checks if a value was already removed so as not to remove it again and updates the main domain and its neighbors, but in case it reaches an inconsistent assignment in which the size of the days is zero it takes a step back and reassigns with what was initially due to a copy that is performed within the function. 
	forward_checking(self,speaker_id,day_id,hour_id)
* least_constrained_value : Function that orders the neighbors of a speaker according to its domain, the amount of consisten values taking into account that they are not assigned, uses a list of tuples in which is saved the days and the sum of amounts of consisten values of all its neighbors returns this list ordered from highest to lowest, using the sort function that orders according to the sum of its consisten values. 
	least_constrained_value(self,speaker_id)
* domain_touched : Function that returns true or false if a neighbor of a specific speaker was played, taking into account that a day or time was removed from that neighbor. 
	domain_touched(self,speaker,neighbor)
  
* arc_consistency : Function that verifies if the neighbors of the neighbors would be touched in its domain causing an inconsistent assignment, taking into account that a specific day and time is assigned, to perform this heuristic a list of tuples that simulates a queue is used. 

* backtrack_search: Function that counts the number of existing domains of each speaker and performs a backtrack according to how many speakers exist.

* backtrack: Function that is in charge of assigning schedules to the speakers with the restrictions of not being able to have two consecutive schedules, that two speakers cannot speak at the same time and on the same day, selects a speaker with less number of domains and then orders the domain variables from highest to lowest in terms of the number of domains that exist in their neighbors, for each domain test which gives a consistent value and assigns it.  


### CLASS DIAGRAM 





![DiagramaClases drawio](https://user-images.githubusercontent.com/74753713/139964523-a06e386d-700b-4d34-a950-ef8bbace41ed.png)









## EXPERIMENTS :round_pushpin:

### DISCLAIMER 
The following experiments focus on the backtrack algorithm using forward checking so that the backtrack algorithm implemented with arc consistent is used for state and time counting so that it can be compared to a simple backtrack with forward checking. 

#### 1. EXPERIMENTS EJECUTION
#### :arrow_down_small: Experiments and results:

------------------------------------------------------------------------------------------------------------------------------------------
##### EXPERIMENT I
Testing with a minimum exhibitor population that has all the available schedules and there are repeats from the same area.
Time of ejecution: 0.079323
,States visited: 234

Name | Area | Nationality |  Day |  Hour 
 :---: |  :---: | :---: | :---: | :---: 
Juan | Ingenieria de Software |  Boliviano |  Lunes |  9
Jose | Sistemas Inteligentes | Argentino | Lunes | 9
Ana | Seguridad de Sistemas | Ecuatoriana |Lunes | 9
Luis | Sistemas Inteligentes|Peruano|Lunes|10
Ana| Sistemas Inteligentes|Barbados|Lunes|11
Roberto|Sistemas Inteligentes|Colombia|Lunes|12


#### EXPERIMENT II
Testing with a minimum exhibitor population with reduced schedules, but with more than one exhibitor in the same area.
Time of ejecution: 0.04678299999999999
,States visited: 139

Name | Area | Nationality |  Day |  Hour 
 :---: |  :---: | :---: | :---: | :---: 
Juan|Ingenieria de Software|Boliviano|Lunes|9
Jose|Sistemas Inteligentes|Argentino|Lunes|9
Ana|Seguridad de Sistemas|Ecuatoriana|Lunes|9
Luis|Sistemas Inteligentes|Peruano|Martes|15
Ana|Sistemas Inteligentes|Barbados|Jueves|9
Roberto|Sistemas Inteligentes|Colombia|Jueves|10


#### EXPERIMENT III
Experiment testing with a larger population and having a preference of one speaker on the same day and also two hours in a row.
Time of ejecution: 0.1276432
,States visited: 234

Name | Area | Nationality |  Day |  Hour 
 :---: |  :---: | :---: | :---: | :---: 
Juan|Ingenieria de Software|Boliviano|Lunes|9
Jose|Sistemas Inteligentes|Argentino|Lunes|9
Ana|Seguridad de Sistemas|Ecuatoriana|Jueves|17
Luis|Sistemas Inteligentes|Peruano|Lunes|10
Anahi|Sistemas Inteligentes|Barbados|Lunes|11
Roberto|Sistemas Inteligentes|Colombia|Lunes|12
Ana|Seguridad de Sistemas|Ecuatoriana|Miercoles|9
Carlos|Ingenieria de Software|Boliviano|Viernes|17
Melany|Sistemas Inteligentes|Boliviano|Lunes|15
Esteban|Ingenieria de Software|Boliviano|Viernes|18
Wilson|Seguridad de Sistemas|Boliviano|Miercoles|10

------------------------------------------------------------------------------------------------------------------------------------------


#### 2. COMPARISON OF TIMES AND STATES VISITED IN THE EXPERIMENTS 


#### :arrow_down_small: Experiments and results:
  
Experiment Number | Type of algorithm |  Time of ejecution |  States Visited
  :---: |  :---: | :---: | :---: 
  I 	|  Backtrack |	0.07964880000000002 | 234 
  IV 	|  Backtrack with ARC |	0.08221869999999998 | 234 
  II 	|  Backtrack |	0.04674400000000001 | 139 
  V 	|  Backtrack with ARC |	0.045838900000000016 | 141
  III	|  Backtrack |	0.13892569999999999 | 234
  VI 	|  Backtrack with ARC |	0.13714610000000005 | 236 

This experiment seeks to compare the number of states visited and the execution time, either using a backtrack with forward checking or backtrack with Arc Consistency, two experiments are associated with the same initial values, for example 
Experiments I and IV, II and V, III and VI have the same initial states and the only thing that varies are the backtrack algorithms with which they are executed.
In the comparative table it can be seen that the backtrack algorithm that uses the forward checking is the one that visits less states, this because this algorithm only visits its neighbors and not its neighbors of its neighbors as does the Arc consistency algorithm, this is not always convenient because it does not predict the future but only to a later state, in another case the one that runs a little faster is the backtrack algorithm with ARC consistency most likely because it predicts almost more than one state after the neighbor and this prevents the evaluation of this state.


------------------------------------------------------------------------------------------------------------------------------------------



#### 3. COMPARISON OF STATES VISITED WITH TOTAL NUMBER OF DOMAINS FOR ALL EXHIBITORS 

Experiment Number | Total Number Domain Of Speakers |  States visited Experiment Backtrack |  States Visited Experiment BackTrack Arc
  :---: |  :---: | :---: | :---: 
  I and IV 	|  270 |	234 | 234 
  II and V 	|  160 |	139 | 141 
  III and VI 	|  283 |	234 | 236 

The following table shows the number of states visited by each backtrack algorithm, either forward checking or arc consistency, in which it can be seen that both follow the trend of visiting almost all domains of all exhibitors, but even more the backtrack algorithm with arc consistency to update its domain, which could be associated to a very close algorithm which is the dfs. 


## CONCLUSION
BackTrack in all the resulting experiments has shown to be an algorithm that at first sight with not very dense data works in a correct way assigning the schedules taking into account the restrictions which are that two exhibitors of the same area do not give a presentation in the same hour and do not give two talks consecutively, But when increasing this population of exhibitors tends to cause problems and does not always reach a consistent allocation, this is probably due to the way of implementing the selection criteria because not always all criteria tend to seek optimality, they are mostly search criteria as long as there is a not so complex solution.
The backtrack implemented in the practice has the function to see how many exhibitors are and according to the size it assigns schedules one by one until it finds a consistent assignment or until it cannot make a backtrack again, for the assignment of a variable it uses the mrv algorithm which chooses the exhibitor with less days and hours available to perform the exhibition and start the selection of this, this is done because it is the most likely exhibitor to cause or enter into a state inconsistent with the other exhibitors because of its time limit. 
After being chosen this exhibitor tries with each possible value of domain that this one can have, looking for the domain that allows the other exhibitors to have more opportunities of days and hours, this is done in the implementation of the least constrained value which returns all these values ordered in a decreasing way by their consistent values that they generate.
When returning this ordered list the backtrack for each domain tests that assigning to the speaker that domain does not cause an inconsistent state among its neighbors if it does not cause it assigns it, After the tests performed on the backtrack it can be inferred that it performs an exhaustive and systematic search throughout the solution space, this makes it very inefficient for the allocation of many schedules, normally its execution time can be obtained with the number of nodes that are visited, its advantage for this type of problem is that it guarantees a solution and this algorithm can be given improvements for the realization of its objective such as pruning or modifying it to a back jumping. 


## BIBLIOGRAPHY
* Class slides


