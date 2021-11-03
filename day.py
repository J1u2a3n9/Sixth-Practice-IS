class Day:
    def __init__(self,day,hours):
        self.day=day
        self.hours=hours
    
    def find_time(self,time):
        try:
            return self.hours.index(time)
        except ValueError :
            return -1
            
    def delete_time(self,index):
        try:
            return self.hours.remove(index)
        except ValueError:
            return -1
    
    def print_hours(self):
        print(self.hours)
    