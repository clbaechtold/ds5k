import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(3,3), columns=['A','B','C'])

# subset the columns by column name
df[['A','C']]

# subset columns by attribute
df.A

# select row 0 using range
df[0:1]
# select rows 0-2 using range
df[0:3]

# selecting using index and .iloc
df.iloc[1]

# subset based on boolean Value
df[df.A > 0]

# sort and store in the df variable
df.sort_values(by='A', inplace=True)

#locate rows 0-2, columns 0-1
df.iloc[:3,:2]
