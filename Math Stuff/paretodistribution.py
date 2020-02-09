import random
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style


people = ['Newton', 'Maxwell', 'Gauss', 'Pythogarus', 'Leibniz', 'Reimann','Taylor', 'Fibonnaci', 'Napier', 'Bernoulli']

peoplewithmoney= {person:10  for person in people}
print(peoplewithmoney)

plt.bar(peoplewithmoney.keys(), peoplewithmoney.values(), color='g')
plt.show()

def Trade(Peoplewithmoney, therepeat=0):
    for r in range(therepeat):
        for i in range(len(Peoplewithmoney)-1):
            people=list(Peoplewithmoney.keys())
            person1=random.choice(people)
            people.remove(person1)
            person2=random.choice(people)
            if Peoplewithmoney[person2]>0:
                Peoplewithmoney[person1]+=1
                Peoplewithmoney[person2]-=1
            else:
                del Peoplewithmoney[person2]
    return Peoplewithmoney
