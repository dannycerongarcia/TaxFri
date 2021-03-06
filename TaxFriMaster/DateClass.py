'''
Created on Jan 24, 2019

@author: DANNY
'''
import datetime
from calendar import month
from _datetime import date

class DateClass(object):
    
    def __init__(self, month =None,Day=None,year =None):

        self.month = month
        self.Day = Day
        self.year = year
        
        
            
    
    def __str__(self):
        if(self.Day==None  and self.month == None and self.year == None):
                                            #covets date to a string
            # return datetime.datetime.today().isoformat()
            return datetime.datetime.today().strftime("%Y/%m/%d")

        else:
            return self.year + "/" + self.month + "/" + self.Day
        
        
    
    #Might need to convert the the format
    def get_month(self):
        if(self.month == None):
            return date.today().month
        else:
            return self.month
    def set_month(self,new_month):
        self.month = new_month
    
    def get_day(self):
        if(self.Day == None):
            return date.today().day
        else:
            return self.Day
    def set_day(self,new_day):
        self.Day = new_day
    
    def get_year(self):
        if(self.year == None):
            return date.today().year
        else:
            return self.year
    def set_year(self,new_year):
        self.year = new_year
    