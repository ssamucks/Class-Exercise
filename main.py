from Gerenciador import GerenciadorAntiViloes

def menu():
    print("\n=== GERENCIADOR DE ANTIVILÕES ===")
    print("1 - Adicionar AntiVilão")
    print("2 - Listar AntiVilões")
    print("3 - Editar AntiVilão")
    print("4 - Remover AntiVilão")
    print("5 - Contar AntiVilões")
    print("6 - Atacar com AntiVilão")
    print("7 - Defender com AntiVilão")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    gerenciador = GerenciadorAntiViloes()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do AntiVilão: ")
            armamento = input("Armamento: ")
            fraqueza = input("Fraqueza: ")
            gerenciador.adicionar(nome, armamento, fraqueza)
            print(f"{nome} adicionado com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de AntiVilões ---")
            for descricao in gerenciador.listar():
                print(descricao)

        elif opcao == "3":
            nome = input("Digite o nome do AntiVilão que deseja editar: ")
            novo_armamento = input("Novo armamento (ou Enter para não alterar): ")
            nova_fraqueza = input("Nova fraqueza (ou Enter para não alterar): ")
            print(gerenciador.editar(nome, novo_armamento or None, nova_fraqueza or None))

        elif opcao == "4":
            nome = input("Digite o nome do AntiVilão que deseja remover: ")
            print(gerenciador.remover(nome))

        elif opcao == "5":
            print(f"Quantidade de AntiVilões: {gerenciador.contar()}")

        elif opcao == "6":
            nome = input("Qual AntiVilão deve atacar? ")
            av = gerenciador.buscar(nome)
            if av:
                print(av.ataque())
            else:
                print("AntiVilão não encontrado.")

        elif opcao == "7":
            nome = input("Qual AntiVilão deve se defender? ")
            av = gerenciador.buscar(nome)
            if av:
                print(av.defesa())
            else:
                print("AntiVilão não encontrado.")

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()