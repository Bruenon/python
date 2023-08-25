from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}.')
print(f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}.')
print(f'O ângulo de {angulo} tem a Tangente de {tangente:.2f}.')
