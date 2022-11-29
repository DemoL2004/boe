import pandas as pd 

carinfo={
 "car":["tata","maruthi","benz","audi"],
"year":[1971,1978,1999,2000],
"color":["black","red","white","blue"]
   }
pdinfo=pd.DataFrame(carinfo)
print(pdinfo)
print("\n")

info=pd.Series(carinfo)
print(info)
print("\n")

print(pdinfo.columns)
print("\n")

print(pdinfo.index)
print("\n")

pdinfo.set_index('year', drop=True ,inplace=True)
print(pdinfo)
print("\n")

pdinfo.reset_index( drop=False,inplace=True)
print(pdinfo)
print("\n")

print(pdinfo['year'].head())
print("\n")

print(pdinfo[['car','year']].head())
print("\n")

print(pdinfo[3:5])
print("\n")

print(pdinfo.loc[1:4,['car','year']].head())
print("\n")

print(pdinfo.loc[[1,3]])
print("\n")

print(pdinfo['year'].head(2))
print("\n")


