from math import radians, sin, cos, tan
an = float(input("Qual o ângulo? "))
s = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, s, ))
c = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, c, ))
t = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, t, ))



