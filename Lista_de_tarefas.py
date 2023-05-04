lista = ["banana"]

def colocar(item):
    lista.append(item)


def tirar(item):
    lista.remove(item)

#def marcar_concluido(item):


while True:
    print("\nLista de tarefas \n================")

    for x in range(len(lista)):
        print(f"{x+1}- {lista[x]}")

    print("================")

    x = int(input("O que deseja fazer agora? \n 1- Adicionar\n 2- Excluir\n 3- Sair\n "))

    if x == 1:
        a = input("O que deseja adicionar?")
        colocar(a)
    elif x == 2:
        a = input("Qual item deseja excluir(nome do item)?")
        tirar(a)
    #elif x == 3:
    #   a = input("Qual item deseja concluir(nome do item)?")
    #    marcar_concluido(a)
    elif x == 3:
        print("Saindo...")
        break

