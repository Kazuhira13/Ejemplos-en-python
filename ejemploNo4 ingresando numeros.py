a = float(input('primer dato: '))
b = float(input('segundo dato: '))
c = float(input('tercero dato: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('el area de los triangulos es de %0.3f'%area)