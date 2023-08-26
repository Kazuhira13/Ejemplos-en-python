year = 2000
if (year % 400 ==0) and (year % 100 ==0):
    print("{} es año bisiesto".format(year))
elif (year % 4 ==0) and (year % 100 !=0):
    print("{} es año bisiesto")
else:
    print("{} no es año bisiesto".format(year))
