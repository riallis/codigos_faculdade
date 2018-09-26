"""
    Fórmula Isidoro para encontrar números perfeitos
    Author: Riallis da Silva França
    Faculdade das Américas - FAM
"""

import math

tamanho = 150  


def numero_primo(n):  # ' Para verificar se número é primo

    if (n <= 3):
        return True
    Nsqrt = math.sqrt(n)
    contador = 3
    while (contador <= Nsqrt):
        if n % contador == 0:
            return False
        contador += 2
    return True


for numero in range(2, tamanho):

    potencia = ((math.pow(2, numero)) - 1)  # 2 elevado a numero e depois subitraido - 1
    primo = numero_primo(potencia)
    if (primo):  # se a função numero_primo retornar True entra no if
        print(potencia * (math.pow(2, (numero - 1))), " eh perfeito !!!")
        # então 2 elevado a numero e depois subitraido - 1, vezes, 2 elevado a numero - 1 é um número perfeito

exit(0)
