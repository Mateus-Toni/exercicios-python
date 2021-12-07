medida = int(input('escreva uma medida em metros: '))
km = medida/1000
hm = medida/100
am = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print("a medida de {} metros equivale a: ".format(medida))
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} am'.format(am))
print('{} dm'.format(dm))
print('{} cm'.format(cm))
print('{} mm'.format(mm))