a = [1, 2, 3, 4, 5]
name = []
for i in range(len(a)):
    globals()['variable{}'.format(i)] = [x for x in range(len(a))]
    name.append(globals()['variable{}'.format(i)])

print(name)

import pandas as pd

df = pd.DataFrame()

print(df)