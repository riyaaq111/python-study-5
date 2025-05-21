#convert the float to an integer
temp=56.8926
result=round(temp)
print(result)
#convert the float to give result 56.89
temp=56.8926
result=round(temp,2)
print(result)
#convert the float to give result 56.893
temp=56.8926
result=round(temp,3)
print(result)
#convert the float to give 56.8926 to 8.926
temp=56.8926
temp=str(temp)
print(temp)
temp=temp


#convert 111.0789 to 78.9
temp=111.0789
temp=str(temp)
print(temp)
temp=(temp[5:])
print(temp)
temp=f"{temp[0:2]}.{temp[2]}"