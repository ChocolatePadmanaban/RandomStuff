import pandas as pd
import numpy as np

df = pd.DataFrame([[260, "best"],[520,"sci"],[260,"sci"]],columns=['movieId','tag'])
print("Dummy DataFrame: \n", df)


movieId, tags= list(df['movieId'].unique()), list(df['tag'].unique())
dfmatrix= pd.DataFrame(np.zeros((len(movieId),len(tags)+1),dtype=int), columns=['movieID']+tags)
# dfmatrix['movieID'][1]= 54
for i, movie in enumerate(movieId):
    listoftag = df.tag[df['movieId']==movie]
    dfmatrix.movieID[i]= movie
    for tag in listoftag:
        dfmatrix[tag][i]=1

print("\n \n dfmatrix \n",dfmatrix)
