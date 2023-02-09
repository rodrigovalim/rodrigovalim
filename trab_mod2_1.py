resultados = []
cand = []
sair = 'n'
while sair != 's':
        print("Nota da avaliação entrevista:")
        e = int(input())
        print("Nota da avaliação teócica:")
        t = int(input())
        print("Nota da avaliação prática:")
        p = int(input())
        print("Nota da avaliação de soft skills:")
        s = int(input())
        resultados.append(f"e{format(e)}_t{format(t)}_p{format(p)}_s{format(s)}")
        print("Deseja concluir a busca? s/n")
        sair = input()

e = int(input('por favor insira a nota mínima da entrevista:'))
t = int(input('por favor insira a nota mínima  do teste teorico:'))
p = int(input('por favor insisra a nota  mínima do teste pratico:'))
s = int(input('por favor insira a nota mínima do teste de soft:'))
for i  in resultados:
    if int(i[1]) >= e and int(i[4]) >= t and int(i[7]) >= p and int(i[10]) >= s:
        print('achei o candidato:')
        print('resultados:',i[1],i[4],i[7],i[10])
    else:
        print('Não achei o candidato com essa nota:')

        print('resultados:',i[1],i[4],i[7],i[10])








