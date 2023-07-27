# Cadastro de colaborador
def cadastrar_colaborador(id):
    nome = input("Nome do colaborador: ")
    setor = input("Setor do colaborador: ")
    salario = float(input("Salário do colaborador: "))

    colaborador = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso.")

# Consulta de colaboradores
def consultar_colaborador():
    opcao = int(input("Opções de consulta:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\nEscolha uma opção: "))

    if opcao == 1:
        for colaborador in lista_colaboradores:
            print("ID:", colaborador["id"])
            print("Nome:", colaborador["nome"])
            print("Setor:", colaborador["setor"])
            print("Salário:", colaborador["salario"])
            print("--------------------")
    elif opcao == 2:
        id_consulta = int(input("Digite o ID do colaborador: "))
        encontrado = False
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_consulta:
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                encontrado = True
                break
        if not encontrado:
            print("Colaborador não encontrado.")
    elif opcao == 3:
        setor_consulta = input("Digite o setor: ")
        encontrados = False
        for colaborador in lista_colaboradores:
            if colaborador["setor"] == setor_consulta:
                print("ID:", colaborador["id"])
                print("Nome:", colaborador["nome"])
                print("Setor:", colaborador["setor"])
                print("Salário:", colaborador["salario"])
                encontrados = True
                print("--------------------")
        if not encontrados:
            print("Nenhum colaborador encontrado no setor especificado.")
    elif opcao == 4:
        return
    else:
        print("Opção inválida.")

# Remover funcionário
def remover_colaborador():
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    removido = False
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            removido = True
            break
    if not removido:
        print("Colaborador não encontrado.")

# Variáveis iniciais
lista_colaboradores = []
id_global = 0

# Print de boas-vindas
print("Bem-vindo ao sistema de gerenciamento de pessoas do Nicolas Romancini Tarouco Silveira!")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    opcao_menu = int(input("Escolha uma opção: "))

    if opcao_menu == 1:
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_menu == 2:
        consultar_colaborador()
    elif opcao_menu == 3:
        remover_colaborador()
    elif opcao_menu == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
