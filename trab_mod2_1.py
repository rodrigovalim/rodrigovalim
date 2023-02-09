#entrevistaX teste_teoricoX teste_praticoX soft+skillsX

def candidato():
    sair = "não"
    while sair != "sim":
        print("Nome do candidato:")
        cand = input()
        print("Nota da entrevista:")
        e = int(input())
        print("Nota da avaliação teócica:")
        t = int(input())
        print("Nota da avaliação prática:")
        p = int(input())
        print("Nota da avaliação de soft skills:")
        s = int(input())
        resultado.append[cand, f"e{format(e)}_t{format(t)}_p{format(p)}_s{format(s)}"]
        print("Deseja concluir a busca? sim/nao")
        sair = input()


resultado = []
candidato()
print(resultado)







