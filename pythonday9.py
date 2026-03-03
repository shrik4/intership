import pandas as pd
data=pd.Series([1,2,4,8])
# print(data)

data={'name':['karan','prayag','shrikar'],
      'age':[29,27,None],
      'sal':[30000,28000,12000]}
df=pd.DataFrame(data)
# print(df)



# df.head(2)
# print(df.head(2))
# print(df.tail())
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.isnull())
# print(df.dropna())
# print(df.fillna('age'))
print(df.loc[:])