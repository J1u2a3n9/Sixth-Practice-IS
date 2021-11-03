import copy
from day import Day
class Speaker:
    def __init__(self,name,area,nationality,day,assigned,number_domain):
        self.name = name
        self.area=area
        self.nationality=nationality
        self.day=day
        self.assigned=assigned
        self.number_domain=number_domain

    def get_day(self,day):
        try:
            if (isinstance(self.day,list)==True and day<len(self.day)):
                return self.day[day].day
            else:
                if (isinstance(self.day,Day)==True):
                     return self.day.day
        except ValueError :
            return -1
    
    def get_days(self):
        return self.day

    def get_day_string(self,day_id):
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

    
    def delete_day(self,day):
        try:
            if (isinstance(self.day,list)==True and day<len(self.day)):
                del self.day[day]
            else:
                if (isinstance(self.day,Day)==True):
                    if (self.day.day==self.get_day_string(day)):
                        del self.day
                
        except ValueError :
            return -1

    def get_hour(self,day,hour):
        try:
            return self.day[day].hours.index(hour)
        except ValueError :
            return -1

    def get_hours(self,day):
        if (isinstance(self.day,list)==True and len(self.day)>0):
            return self.day[day].hours
        else :
            return self.day
    
    def get_day_object(self,list_day,index_day):
        day_string=self.get_day_string(index_day)
        pos=0
        for day in list_day:
            if day_string == day.day :
                return pos
            pos=pos+1
        return -1

    def delete_hour(self,day,hours):
        if (isinstance(hours,list)==True):
            hour=hours[0]
        else:
            hour=hours
        try:
            if(day<=(len(self.day)-1)):
                index_day=self.get_day_object(self.day,day)
                days=copy.deepcopy(self.day[index_day])
                days.hours.remove(hour)
                return days
            else:
                if(len(self.day)==1 and len(self.day[0].hours)==1 ):
                    index_day=self.get_day_object(self.day,day)
                    if index_day > -1:
                        days=copy.deepcopy(self.day[index_day])
                        if (days.hours==hour):
                            days.hours=0
                        return days
                else:
                    if(len(self.day)==1 and len(self.day[0].hours)>1 ):
                        index_day=self.get_day_object(self.day,day)
                        if index_day > -1:
                            days=copy.deepcopy(self.day[index_day])
                            days.hours.remove(hour)
                            return days
                    else:
                        index_day=self.get_day_object(self.day,day)
                        if index_day > -1:
                            days=copy.deepcopy(self.day[index_day])
                            days.hours.remove(hour)
                            return days 
            
                                      
        except ValueError :
            index_day=self.get_day_object(self.day,day)
            days=copy.deepcopy(self.day[index_day])
            return days
    
        