import math
from turtle import *

def hearta(k):
    return 12* math.sin(k)**3

def heart(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
            
speed(6000)          
bgcolor("black") 

for i in range(60000):
     goto(hearta(i)*20,heart (i )*20)
     for j in range(5):
         color("red")
     goto(0,0)       
done()        
   
            
                
