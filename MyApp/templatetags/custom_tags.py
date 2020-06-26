
import datetime
from datetime import date,datetime
from django import template
from django.utils.dateformat import format

register = template.Library()

@register.filter
def state_of_event(e):
    now=datetime.now()
    #m=now.month
    #return m
    #cur_time=now.strftime("%H:%M:%S")
    datetime_object = datetime.strptime(e.month, "%B")
    event_month = datetime_object.month

    date1=datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)
    date2=datetime(e.year,event_month,e.date,e.time.hour,e.time.minute,e.time.second)
    date3=datetime(e.End_time.year,e.End_time.month,e.End_time.day,e.End_time.hour,e.End_time.minute,e.End_time.second)
    if(date2 < date1 and date3 > date1): 
        return 0
    elif(date2 < date1):
        return -1
    elif(date2 > date1):
        return 1