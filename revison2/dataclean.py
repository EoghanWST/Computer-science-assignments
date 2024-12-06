import pandas as pd
#When we wish to use pandas we will type pd instead of pandas
#df = pd.read_csv('unclean_data 1.csv')
#This will give an error message
#Pandas expects to get a utf-8 encoded file by defaul

#overwrite the default encoding of utf-8
df = pd.read_csv('unclean_data 1.csv',encoding='ANSI')
print(df.columns)

df.columns = df.columns.str.upper()
print(df.columns)

#df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
#Case sensitive 'DURATION' is not the same as 'duration'
df = df.rename(columns = {'DURATION':'TIME'})
print(df.columns)

print(df.isnull())

pd.set_option('display.max_columns', None)
print(df.isnull())

print(df.isnull().any())

print(df.isnull().sum())

print(df.isnull().sum().sum())

print(df.head(5))

df = df.fillna(0)
print(df.head(5))

print(df.head(5))

new_values = {"TIME": 100, "FACENUMBER_IN_POSTER": -999}
df=df.fillna(value=new_values)

mean_of_TIME = df['TIME'].mean()
df['TIME'] = df.TIME.fillna(mean_of_TIME)

df.dropna(inplace=True)

df = df.dropna()
