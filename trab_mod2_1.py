#entrevistaX teste_teoricoX teste_praticoX soft+skillsX

def candidato():
    sair = "não"
    while sair != "sim":
        print("Nome do candidato:")
        cand = input()
        print("Nota da entrevista:")
        e = float(input())
        print("Nota da avaliação teócica:")
        t = float(input())
        print("Nota da avaliação prática:")
        p = float(input())
        print("Nota da avaliação de soft skills:")
        s = float(input())
        resultado.append([cand, f"e{format(e)}_t{format(t)}_p{format(p)}_s{format(s)}"])
        print("Deseja concluir a busca? sim/nao")
        sair = input()


resultado = []
candidato()
if resultado[0][1] >= resultado[1][1]:
    print(resultado[0])
else:
    print(resultado)







