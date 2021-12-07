import math
ang = float(input('Digite o ângulo: '))
print('para um ângulo de {} temos: '.format(ang))
print('seno de {} é {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('cosseno de {} é {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('tangente de {} é {:.2f}'.format(ang, math.tan(math.radians(ang))))
