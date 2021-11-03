from speaker import Speaker
from day import Day
import copy
import time
import timeit



class Event:
    def __init__(self,speakers):
        self.speakers=speakers
        self.states_visited=0

    def get_hour_index(self,hour):
        if hour==9:
            return 0
        if hour==10:
            return 1
        if hour==11:
            return 2
        if hour==12:
            return 3
        if hour==15:
            return 4
        if hour==16:
            return 5
        if hour==17:
            return 6
        if hour==18:
            return 7
    
    def get_day(self,day_id):
        if day_id==0:
            return "Lunes"
        if day_id==1:
            return "Martes"
        if day_id==2:
            return "Miercoles"
        if day_id==3:
            return "Jueves"
        if day_id==4:
            return "Viernes"

    
    def get_max_value(self,list):
        max=0
        for item in list:
            if item.consistent_value >= max:
                max=item.consistent_value
        return max
        
    def get_number_day(self,day):
        if day=="Lunes":
            return 0
        if day=="Martes":
            return 1
        if day=="Miercoles":
            return 2
        if day=="Jueves":
            return 3
        if day=="Viernes":
            return 4


    #Obtiene las horas de un expositor pasandole el id del expositor y la posicion del dia especifico
    def get_hours(self,speaker_id,day_id):
        return self.speakers[speaker_id].get_hours(day_id)



    #Elimina una hora de un dia especifico de un expositor
    def delete_hour(self,speaker_id,day_id,hour):
        hour_id=hour
        speaker=copy.deepcopy(self.speakers[speaker_id])
        speaker_oficial=Speaker(speaker.name,speaker.area,speaker.nationality,speaker.day,speaker.assigned,speaker.number_domain)
        if(len(speaker_oficial.day)>=1):
            i=0
            for day in speaker_oficial.day:
                if(day.day==self.get_day(day_id)):
                    value=speaker_oficial.delete_hour(day_id,hour_id)
                    speaker_oficial.day[i].hours=value.hours
                i=i+1
        self.speakers[speaker_id]=speaker_oficial



    #Elimina un dia incluyendo todas sus horas de un expositor 
    def delete_day(self,speaker_id,day_id):
        self.speakers[speaker_id].delete_day(day_id)
    
    # Devuelve el tamaño de una lista
    def get_size(self,lista):
        return len(lista)


    def clean_data(self,days):
        i=0
        for day in days:
            if day==None:
                days.pop(i)
            i=i+1
        return days


    # Setear cantidad de valores de dominio de un speaker
    def set_domain_number(self,speaker_id):
        speaker=self.speakers[speaker_id]
        dirty_days=speaker.get_days()
        days=self.clean_data(dirty_days)
        size_days=self.get_size(days)
        size_hours=0
        for day in self.speakers[speaker_id].day:
            if day!=None:
                size_hours=size_hours+self.get_size(day.hours)
        total_acount=size_days+size_hours
        self.speakers[speaker_id].number_domain=total_acount

    # Contar cantidad de valores de dominio de un speaker
    def get_domain_number(self,speaker_id):
        return self.speakers[speaker_id].number_domain


    #Escoger variable no asignada, que tenga menos dias o menos horas
    def mrv(self):
        new_list=[]
        for speaker in self.speakers:
            if speaker.assigned == False:
                new_list.append(speaker.number_domain)
            else:
                new_list.append(100000000000000000000)
        number_min=min(new_list)
        index_min=new_list.index(number_min)
        return self.speakers[index_min]
    
    # Obtener vecinos de un speaker segun su area
    def neighbors(self,area,speaker_id):
        neighbors=[]
        for speaker in self.speakers:
            if speaker.area==area and self.speakers[speaker_id]!=speaker and speaker.assigned==False:
                neighbors.append(speaker)
        return neighbors

    #Forward Checking es poner dia y hora y quitar esa hora y dia de vecinos
    #Ver si ya se quito un valor para no quitarlo otra vez 
    #Actualiza el dominio principal y de sus vecinos
    def forward_checking(self,speaker_id,day_id,hour_id):
        speakers_aux=copy.deepcopy(self.speakers)
        speaker=self.speakers[speaker_id]
        res=False
        if (len(speaker.day)>=1):
            day=self.get_day(day_id)
            for days in speaker.day:
                if(day in days.day):
                    res=res or True
            if (res==True):
                speaker.assigned=True
                day_oficial=Day(day,hour_id)
                list_day=[]
                list_day.append(day_oficial)
                speaker.day=list_day
                neighbors=self.neighbors(speaker.area,speaker_id)
                index=0
                for speaker in neighbors:
                    if (self.get_size(speaker.day)!=0):
                        index=self.speakers.index(speaker)
                        self.delete_hour(index,day_id,hour_id)
                    else:
                        self.speakers=speakers_aux
        else:
            self.speakers=speakers_aux

            
        
        

    def least_constrained_value(self,speaker_id):
        all_consistent_values=[]
        speakers_temp_aux=copy.deepcopy(self.speakers)
        speaker=self.speakers[speaker_id]
        area=self.speakers[speaker_id].area
        if (isinstance(speaker.day,list)==True):
            for day in speaker.day:
                if day!=None:
                    for hour in day.hours:
                        self.states_visited=self.states_visited+1
                        speakers_temp=copy.deepcopy(self.speakers)
                        id_day=self.get_number_day(day.day)
                        self.forward_checking(speaker_id, id_day, hour)
                        consistent_values=0
                        for neighbor in self.neighbors(area,speaker_id):
                            index=self.speakers.index(neighbor)
                            self.set_domain_number(index)
                            consistent_values=consistent_values+self.get_domain_number(index)
                        day_value=self.get_day(id_day)
                        hour_value=hour
                        hour_list=[]
                        hour_list.append(hour_value)
                        oficial_day=Day(day_value,hour_list)
                        tuple_to_use=(oficial_day,consistent_values)
                        all_consistent_values.append(tuple_to_use)
                        self.speakers=speakers_temp   
        all_consistent_values.sort(key=lambda x:x[1], reverse=True)
        self.speakers=speakers_temp_aux
        return all_consistent_values


    def least_constrained_value_arc(self,speaker_id):
        all_consistent_values=[]
        speakers_temp_aux=copy.deepcopy(self.speakers)
        speaker=self.speakers[speaker_id]
        area=self.speakers[speaker_id].area
        if (isinstance(speaker.day,list)==True):
            for day in speaker.day:
                if day!=None:
                    for hour in day.hours:
                        self.states_visited=self.states_visited+1
                        speakers_temp=copy.deepcopy(self.speakers)
                        id_day=self.get_number_day(day.day)
                        self.arc_consistency(speaker_id,day)
                        consistent_values=0
                        for neighbor in self.neighbors(area,speaker_id):
                            index=self.speakers.index(neighbor)
                            self.set_domain_number(index)
                            consistent_values=consistent_values+self.get_domain_number(index)
                        day_value=self.get_day(id_day)
                        hour_value=hour
                        hour_list=[]
                        hour_list.append(hour_value)
                        oficial_day=Day(day_value,hour_list)
                        tuple_to_use=(oficial_day,consistent_values)
                        all_consistent_values.append(tuple_to_use)
                        self.speakers=speakers_temp   
        all_consistent_values.sort(key=lambda x:x[1], reverse=True)
        self.speakers=speakers_temp_aux
        return all_consistent_values


    
    def domain_touched(self,speaker,neighbor,day_id,hour_id):
        touched=False
        if (isinstance(neighbor.day,list)==True):
            for day in neighbor.day:
                for hour in day.hours:
                    if hour==speaker.day[0].hours and day.day==speaker.day[0].day:
                        if (self.get_size(neighbor.day)!=0):
                            index=self.speakers.index(neighbor)
                            day_id=neighbor.day.index(day)
                            self.delete_hour(index,day_id,hour)
                            touched=True
        return touched
           

    def arc_consistency(self,speaker_id,day):
        speakers_aux=copy.deepcopy(self.speakers)
        speaker=self.speakers[speaker_id]
        speaker.assigned=True
        day_id=self.get_number_day(day.day)
        hour_id=day.hours[0]
        day_1=self.get_day(day_id)
        day_oficial=Day(day_1,hour_id)
        list_day=[]
        list_day.append(day_oficial)
        speaker.day=list_day
        relation=[]
        index_hour=self.get_hour_index(hour_id)
        neighbors=self.neighbors(speaker.area,speaker_id)
        if (day_oficial.day!=None):
            for neighbor in neighbors:
                tuple_node=(speaker,neighbor)
                relation.append(tuple_node)
            while (relation!=[]):
                speaker_tuple,neighbor_tuple=relation.pop()
                index_neighbor=self.speakers.index(neighbor_tuple)
                if (self.domain_touched(speaker_tuple,neighbor_tuple,day_id,index_hour)==True):
                    if (neighbor.day==[]):
                        return False
                    sub_neighbor=self.neighbors(neighbor.area,index_neighbor)
                    for re_sub_neighbor in sub_neighbor:
                        re_tuple_node=(neighbor,re_sub_neighbor)
                        relation.append(re_tuple_node)
        return True
    
    def complete_assignment(self):
        result=True
        for speaker in self.speakers:
            if speaker.assigned==True:
                result=result and True
            else :
                result=result and False
                return result
        return result

    def valid_assignment(self,index_speaker,day):
        result=True
        copy_neighboards=copy.deepcopy(self.speakers)
        day_id=self.get_number_day(day[0].day)
        hour_id=day[0].hours
        self.forward_checking(index_speaker,day_id,hour_id)
        for speaker in self.speakers:
            if (self.get_size(speaker.day)==0):
                self.speakers=copy_neighboards
                result=False
                return result
        self.speakers=copy_neighboards
        return result


    def backtrack_search(self):
        count=0
        for speaker in self.speakers:
            index=self.speakers.index(speaker)
            self.set_domain_number(index)
        while count<len(self.speakers):
            self.backtrack()
            count=count+1
    

    def backtrack(self):
        if (self.complete_assignment()==True):
            return self.speakers
        speaker_selected=self.mrv()
        index_speaker=self.speakers.index(speaker_selected)
        ordered_domain=self.least_constrained_value(index_speaker)
        for domain in ordered_domain:
            day_id=self.get_number_day(domain[0].day)
            hour_id=domain[0].hours
            if(self.valid_assignment(index_speaker,domain)==True):
                self.forward_checking(index_speaker,day_id,hour_id)
                return self.speakers
            else:
                for speaker in self.speakers:
                    index_speaker_copy=self.speakers.index(speaker)
                    self.delete_hour(index_speaker_copy,day_id,hour_id)
                return False
        return self.speakers

    
    def backtrack_search_arc(self):
        count=0
        for speaker in self.speakers:
            index=self.speakers.index(speaker)
            self.set_domain_number(index)
        while count<len(self.speakers):
            self.backtrack_arc()
            count=count+1

    
    def backtrack_arc(self):
        if (self.complete_assignment()==True):
            return self.speakers
        speaker_selected=self.mrv()
        index_speaker=self.speakers.index(speaker_selected)
        ordered_domain=self.least_constrained_value_arc(index_speaker)
        for domain in ordered_domain:
            day_id=self.get_number_day(domain[0].day)
            hour_id=domain[0].hours
            if(self.valid_assignment(index_speaker,domain)==True):
                self.arc_consistency(index_speaker,domain[0])
                return self.speakers
            else:
                for speaker in self.speakers:
                    index_speaker_copy=self.speakers.index(speaker)
                    self.delete_hour(index_speaker_copy,day_id,hour_id)
                return False
        return self.speakers
        

    def print_solution(self,data):
        print("-------------------------------------------------------------------------------------------------------------",file=data)
        print("------------------------------------------STATES VISITED-----------------------------------------------------",file=data)
        print("States visited: "+str(self.states_visited),file=data)
        for  speaker in self.speakers:
            print(file=data)
            print(file=data)
            print("------------------------------------------SPEAKER INFORMATION-----------------------------------------------------",file=data)
            print("Name: "+speaker.name,file=data)
            print("Area: "+speaker.area,file=data)
            print("Nationality: "+speaker.nationality,file=data)
            print("-----------------------------------------------SCHEDULE-----------------------------------------------------------",file=data)
            for day in speaker.day:
                print("Day: "+day.day,file=data)
                if (isinstance(day.hours,list)==True):
                    for hour in day.hours:
                        print("Hour: "+str(hour),file=data)
                else:
                    print("Hour: "+str(day.hours),file=data)

        print("-------------------------------------------------------------------------------------------------------------",file=data) 
        print(file=data)
        print(file=data)  



    def print_solution_initial(self,data):
        print("-------------------------------------------------------------------------------------------------------------",file=data)
        print("------------------------------------------STATES VISITED-----------------------------------------------------",file=data)
        print("States visited: "+str(self.states_visited),file=data)
        for  speaker in self.speakers:
            print(file=data)
            print(file=data)
            print("------------------------------------------SPEAKER INFORMATION-----------------------------------------------------",file=data)
            print("Name: "+speaker.name,file=data)
            print("Area: "+speaker.area,file=data)
            print("Nationality: "+speaker.nationality,file=data)
            print("-----------------------------------------------SCHEDULE-----------------------------------------------------------",file=data)
            for day in speaker.day:
                print("Day: "+day.day,file=data)
                if (isinstance(day.hours,list)==True):
                    for hour in day.hours:
                        print("Hour: "+str(hour),file=data)
                else:
                    print("Hour: "+str(day.hours),file=data)

        print("-------------------------------------------------------------------------------------------------------------",file=data) 
        print(file=data)
        print(file=data)  


    def print_solution_arc(self):
        print("-------------------------------------------------------------------------------------------------------------")
        print("------------------------------------------STATES VISITED-----------------------------------------------------")
        print("States visited: "+str(self.states_visited))
        for  speaker in self.speakers:
            print()
            print()
            print("------------------------------------------SPEAKER INFORMATION-----------------------------------------------------")
            print("Name: "+speaker.name)
            print("Area: "+speaker.area)
            print("Nationality: "+speaker.nationality)
            print("-----------------------------------------------SCHEDULE-----------------------------------------------------------")
            for day in speaker.day:
                print("Day: "+day.day)
                if (isinstance(day.hours,list)==True):
                    for hour in day.hours:
                        print("Hour: "+str(hour))
                else:
                    print("Hour: "+str(day.hours))

        print("-------------------------------------------------------------------------------------------------------------") 
        print()
        print()      










        
    






        










    


def add_speaker(list,speaker):
    list.append(speaker)


def main():
    data=open("end.txt","w")
    data_start=open("start.txt","w")
    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data)
    print("EXPERIMENT I",file=data)
    print("Testing with a minimum exhibitor population that has all the available schedules and there are repeats from the same area.",file=data)
    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data_start)
    print("EXPERIMENT I",file=data_start)
    print("Testing with a minimum exhibitor population that has all the available schedules and there are repeats from the same area.",file=data_start)

    hours=[9,10,11,12,15,16,17,18]
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",days_list,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Ana","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    events=Event(my_list_speaker)
    events.print_solution_initial(data_start)
    start=timeit.default_timer()
    events.backtrack_search()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time),file=data)
    events.print_solution(data)


    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data)
    print("EXPERIMENT II",file=data)
    print("Testing with a minimum exhibitor population with reduced schedules, but with more than one exhibitor in the same area.",file=data)

    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data_start)
    print("EXPERIMENT II",file=data_start)
    print("Testing with a minimum exhibitor population with reduced schedules, but with more than one exhibitor in the same area.",file=data_start)

    hours=[9,10,11,12,15,16,17,18]
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",days_list,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Ana","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    events=Event(my_list_speaker)
    events.delete_hour(1,1,15)
    events.delete_hour(2,2,10)
    events.delete_hour(0,1,9)
    events.delete_day(0,1)
    events.delete_day(1,3)
    events.delete_day(1,2)
    events.delete_day(3,0)
    events.delete_day(4,1)
    events.delete_day(5,2)
    events.print_solution_initial(data_start)
    start=timeit.default_timer()
    events.backtrack_search()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time),file=data)
    events.print_solution(data)
    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data)



    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data)
    print("EXPERIMENT III",file=data)
    print("Experiment testing with a larger population and having a preference of one speaker on the same day and also two hours in a row.",file=data)

    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data_start)
    print("EXPERIMENT III",file=data_start)
    print("Experiment testing with a larger population and having a preference of one speaker on the same day and also two hours in a row.",file=data_start)


    hours=[9,10,11,12,15,16,17,18]

    consecutiv_hour=[9,10]
    specific_day=Day("Miercoles",consecutiv_hour)
    day_list_2=[]
    day_list_2.append(specific_day)

    consecutiv_hour_2=[17,18]
    specific_day_2=Day("Viernes",consecutiv_hour_2)
    day_list_4=[]
    day_list_4.append(specific_day_2)

    hour_1=[18]
    day_1=Day("Viernes",hour_1)
    day_list_5=[]
    day_list_5.append(day_1)



    hour=[17]
    day=Day("Jueves",hour)
    day_list_3=[]
    day_list_3.append(day)
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",day_list_3,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Anahi","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    speaker_7 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",day_list_2,False,-1)     
    speaker_8 = Speaker("Carlos","Ingenieria de Software","Boliviano",day_list_4,False,-1) 
    speaker_9 = Speaker("Melany","Sistemas Inteligentes","Boliviano",days_list,False,-1) 
    speaker_10 = Speaker("Esteban","Ingenieria de Software","Boliviano",day_list_5,False,-1) 
    speaker_11 = Speaker("Wilson","Seguridad de Sistemas","Boliviano",day_list_2,False,-1) 

    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    add_speaker(my_list_speaker,speaker_7)
    add_speaker(my_list_speaker,speaker_8)
    add_speaker(my_list_speaker,speaker_9)
    add_speaker(my_list_speaker,speaker_10)
    add_speaker(my_list_speaker,speaker_11)
    events=Event(my_list_speaker)
    events.print_solution_initial(data_start)
    start=timeit.default_timer()
    events.backtrack_search()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time),file=data)
    events.print_solution(data)
    print("------------------------------------------------------------------------------------------------------------------------------------------",file=data)


    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("EXPERIMENT IV")
    print("Experiment updating domains with arc consistency in backtrack and least constrained value")
    hours=[9,10,11,12,15,16,17,18]
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",days_list,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Ana","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    events=Event(my_list_speaker)
    start=timeit.default_timer()
    events.backtrack_search_arc()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time))
    events.print_solution_arc()


    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("EXPERIMENT V")
    print("Testing with Arc consitency in backtrack, least constrained value and  and a minimum exhibitor population with reduced schedules, but with more than one exhibitor in the same area.")
    hours=[9,10,11,12,15,16,17,18]
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",days_list,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Ana","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    events=Event(my_list_speaker)
    events.delete_hour(1,1,15)
    events.delete_hour(2,2,10)
    events.delete_hour(0,1,9)
    events.delete_day(0,1)
    events.delete_day(1,3)
    events.delete_day(1,2)
    events.delete_day(3,0)
    events.delete_day(4,1)
    events.delete_day(5,2)
    start=timeit.default_timer()
    events.backtrack_search_arc()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time))
    events.print_solution_arc()
    print("------------------------------------------------------------------------------------------------------------------------------------------")

    print("------------------------------------------------------------------------------------------------------------------------------------------")
    print("EXPERIMENT VI")
    print("Experiment testing with Arc consistency in backtrack, least constrained value a larger population and having a preference of one speaker on the same day and also two hours in a row.")
    hours=[9,10,11,12,15,16,17,18]

    consecutiv_hour=[9,10]
    specific_day=Day("Miercoles",consecutiv_hour)
    day_list_2=[]
    day_list_2.append(specific_day)

    consecutiv_hour_2=[17,18]
    specific_day_2=Day("Viernes",consecutiv_hour_2)
    day_list_4=[]
    day_list_4.append(specific_day_2)

    hour_1=[18]
    day_1=Day("Viernes",hour_1)
    day_list_5=[]
    day_list_5.append(day_1)



    hour=[17]
    day=Day("Jueves",hour)
    day_list_3=[]
    day_list_3.append(day)
    day_1 = Day("Lunes",hours)
    day_2 = Day("Martes",hours)
    day_3 = Day("Miercoles",hours)
    day_4 = Day("Jueves",hours)
    day_5 = Day("Viernes",hours)
    days_list=[]
    days_list.append(day_1)
    days_list.append(day_2)
    days_list.append(day_3)
    days_list.append(day_4)
    days_list.append(day_5)
    speaker = Speaker("Juan","Ingenieria de Software","Boliviano",days_list,False,-1) 
    speaker_2 = Speaker("Jose","Sistemas Inteligentes","Argentino",days_list,False,-1) 
    speaker_3 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",day_list_3,False,-1) 
    speaker_4 = Speaker("Luis","Sistemas Inteligentes","Peruano",days_list,False,-1) 
    speaker_5 = Speaker("Anahi","Sistemas Inteligentes","Barbados",days_list,False,-1) 
    speaker_6 = Speaker("Roberto","Sistemas Inteligentes","Colombia",days_list,False,-1) 
    speaker_7 = Speaker("Ana","Seguridad de Sistemas","Ecuatoriana",day_list_2,False,-1)     
    speaker_8 = Speaker("Carlos","Ingenieria de Software","Boliviano",day_list_4,False,-1) 
    speaker_9 = Speaker("Melany","Sistemas Inteligentes","Boliviano",days_list,False,-1) 
    speaker_10 = Speaker("Esteban","Ingenieria de Software","Boliviano",day_list_5,False,-1) 
    speaker_11 = Speaker("Wilson","Seguridad de Sistemas","Boliviano",day_list_2,False,-1) 

    my_list_speaker=[]
    add_speaker(my_list_speaker,speaker)
    add_speaker(my_list_speaker,speaker_2)
    add_speaker(my_list_speaker,speaker_3)
    add_speaker(my_list_speaker,speaker_4)
    add_speaker(my_list_speaker,speaker_5)
    add_speaker(my_list_speaker,speaker_6)
    add_speaker(my_list_speaker,speaker_7)
    add_speaker(my_list_speaker,speaker_8)
    add_speaker(my_list_speaker,speaker_9)
    add_speaker(my_list_speaker,speaker_10)
    add_speaker(my_list_speaker,speaker_11)
    events=Event(my_list_speaker)
    start=timeit.default_timer()
    events.backtrack_search_arc()
    end=timeit.default_timer()
    total_time=end-start
    print("Time of ejecution: "+str(total_time))
    events.print_solution_arc()
    print("------------------------------------------------------------------------------------------------------------------------------------------")




 


if __name__ == '__main__':
    main()