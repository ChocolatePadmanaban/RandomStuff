# Theorm: If a Triangle is created in random then only a Quator of them will be Acute
# We are verifying it using python and numpy

import numpy as np 

ainput = np.random.rand(1000,6)

def CheckAcute(sixpoints):
    """
    this function will get input of six points from which it will check the weather the triangle is acute or obtuse 
    input : list of point for a tiangle
    output : reture if its acute else its false
    """
    a,b,c= sixpoints[:2],sixpoints[2:4], sixpoints[4:]    
    perimeter = [np.linalg.norm(a-b), np.linalg.norm(b-c),np.linalg.norm(c-a)]
    perimeter.sort()
    adj,opp,hyp = perimeter
    return True if hyp**2 < adj**2 +opp**2 else False 

def VCheckAcute(allsix):
    return np.mean(np.array([CheckAcute(i) for i in ainput]))



if __name__ == "__main__":
    print(VCheckAcute(ainput))
