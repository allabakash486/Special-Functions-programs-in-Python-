def Highest_val(var):
    Highest_value = var[0]
    for i in range(1,len(var)):
        if Highest_value < var[i]:
           Highest_value,var[i]=var[i],Highest_value
    return Highest_value
var = [1,1,2,3,4,4,5,6,90]
print(Highest_val(var))