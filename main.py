import pandas as pd
import numpy as np
import random
import os

def filter1(array1, array2):
    for i in range(len(array1)):
        if array1[i] > 35:
            array1[i] = random.randint(array2[i], 35)
    return array1

def filter2(array1, array2, diff):
    for i in range(len(array1)):
        if diff[i] < 0:
            array1[i] = random.randint(5, array2[i]-1)
    return array1

presence = np.random.randint(5, 35, 90)
life_satisfaction = presence + np.random.randint(0, 10, 90)
life_satisfaction = filter1(life_satisfaction, presence)

search = np.random.randint(5, 35, 90)
diff = life_satisfaction - search
search = filter2(search, life_satisfaction, diff)

data = {"Presence": presence, "Search": search, "Life satisfaction": life_satisfaction}
df = pd.DataFrame(data)
df.index = np.arange(1,len(df)+1)

cwd = os.getcwd()
# df.to_csv(os.path.join(cwd, "new.csv"))

print(np.corrcoef(presence, life_satisfaction))
print(np.corrcoef(search, life_satisfaction))