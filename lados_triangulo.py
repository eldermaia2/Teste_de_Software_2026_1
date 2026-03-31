"""Determine os casos de teste para o programa do triângulo
(equilátero, isósceles, escaleno) feito na primeira aula usando o
particionamento por classes de equivalência."""

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores informados não formam um triângulo")