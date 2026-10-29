import random

def list_of_hexa_colors(x):
    color=[]
    char="0123456789abcdef"
    
    for i in range(x):
     r="".join(random.choice(char) for _ in range(6))
     color.append("#"+r)
    return color


