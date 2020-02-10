import random
import math

def aleatorio100():
    
    for i in range(10):
        x = random.random() 
        x = math.trunc(x*100)
        print(x)


aleatorio100()