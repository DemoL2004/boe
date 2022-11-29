import pandas as pd

stdinfo=pd.read_csv("smalldatas.csv")
print(stdinfo)
print("\n")

print(stdinfo.columns)





print("\n")

print(stdinfo.index)
print("\n")

stdinfo.set_index('Rollno', drop=True ,inplace=True)
print(stdinfo)
print("\n")

stdinfo.reset_index( drop=False,inplace=True)
print(stdinfo)
print("\n")

print(stdinfo['Name'].head())
print("\n")

print(stdinfo[['Name','Rollno']].head())
print("\n")

print(stdinfo[3:5])
print("\n")

print(stdinfo.loc[1:4,['Age','Branch']].head())
print("\n")

print(stdinfo.loc[[1,3]])
print("\n")

print(stdinfo['Branch'].head(2))
print("\n")
