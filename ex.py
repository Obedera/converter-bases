valor_user = input('Digite o valor para ser convertido: ')
base_user = int(input('Digite a base do valor: '))

def converter_base_dez(valor, base):
    lista = []
    aux = 0
    valor_final = 0
    for algarismo in valor:
        if algarismo.upper() == 'A':
            lista.append('10')
        if algarismo.upper() == 'B':
            lista.append('11')
        if algarismo.upper() == 'C':
            lista.append('12')
        if algarismo.upper() == 'D':
            lista.append('13')
        if algarismo.upper() == 'E':
            lista.append('14')
        if algarismo.upper() == 'F':
            lista.append('15')
        try:
            lista.append(int(algarismo))
        except ValueError:
            pass 
    
    i = len(lista)-1
    j = 0
    while i>=0:
        aux += (base**i)*int(lista[j])
        valor_final += aux
        j += 1
        i -= 1

    return aux

print(f'O valor convertido para a base 10 é: {converter_base_dez(valor_user, base_user)}')