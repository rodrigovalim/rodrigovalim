resultado = []
lista = []

def candidato():
    while True:
        lista.append(str(input('nome do candidato:')))
        lista.append(int(input('nota e: ')))
        lista.append(int(input('nota t: ')))
        lista.append(int(input('nota p: ')))
        lista.append(int(input('nota s: ')))
        resultado.append(lista[:])
        lista.clear()
        sair = str(input('deseja continuar? s/n: '))
        if sair in 'Nn':
            break

        
        
        
        


candidato()

   #para acessar o indice da sublista [0][1]

if resultado[0][1] > resultado[1][1] and resultado[0][1] > resultado[2][1] and resultado[0][1] > resultado[3][1] and resultado[0][1] > resultado[4][1] and resultado[0][1] > resultado[5][1]:
    print(resultado[0])
else:
    print(resultado)

