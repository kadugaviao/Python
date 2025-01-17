"""
from math import trunc
def numInteiro():
    num = float(input("Digite um número com parte decimal: "))
    print(f"O número digitado foi {num} e sua porção inteira é {trunc(num)}")

numInteiro()
"""

def numInteiro():
    num = float(input("Digite um número: ")) 
    print(f"O número digitado é {num} e a porção inteira é {int(num)}")

numInteiro()
