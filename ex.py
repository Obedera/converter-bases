valor_user = input('Digite o valor para ser convertido: ')
base_user = int(input('Digite a base do valor: '))
base_destino = int(input('Digite a base para o valor convertido: '))

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

def converter_qualquer_base(valor, base):
    lista = []
    while valor>=base:
        lista.append(valor%base)
        valor = int(valor/base)
    lista.append(valor)

    aux = ''
    i = len(lista)-1
    while i>=0:
        if lista[i]<10:
            aux += str(lista[i])
        if lista[i] == 10:
            aux += 'A'
        if lista[i] == 11:
            aux += 'B'
        if lista[i] == 12:
            aux += 'C'
        if lista[i] == 13:
            aux += 'D'
        if lista[i] == 14:
            aux += 'E'
        if lista[i] == 15:
            aux += 'F'
        i -= 1
    
    return aux

valor_base_dez = converter_base_dez(valor_user, base_user)
valor_convertido = converter_qualquer_base(valor_base_dez,base_destino)
print(f'O valor convertido para a base 10 é: {valor_base_dez}')
print(f'O valor convertido para a base {base_destino} é: {valor_convertido}')
