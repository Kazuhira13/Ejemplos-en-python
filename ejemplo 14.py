num = 29


flag= False

if num>1:
    for i in range(2,num):
        if (num % i) ==0:
            flag = True
            break
if flag:
    print(num, "no es un numero primo")
else:
    print(num, "es numero primo")