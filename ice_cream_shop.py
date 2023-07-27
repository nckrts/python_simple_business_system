# Mensagem de boas vindas
print("Bem-vindo sorveteria do Nicolas Romancini Tarouco Silveira!")
total = 0

print("---------------------------------------------Cardápio---------------------------------------------")
print("| N de bolas | Sabor tradicional (tr) |   Sabor Premium (pr)   |    Sabor Especial (es)  |")
print("|          1        |              R$ 6,00            |              R$ 7,00             |              R$ 8,00            |")
print("|          2        |             R$ 10,00           |              R$ 12,00           |             R$ 14,00          |")
print("|          3        |             R$ 14,00           |              R$ 17,00           |             R$ 20,00          |")
print("----------------------------------------------------------------------------------------------------")
    
while True:
    # Recebe o pedido do sorvete e da quantidade
    sabor = input("Digite o sabor desejado: tradicional (tr),  premium (pr), especial (es): ")
    bolas = int(input("Digite a quantidade de bolas de sorvete desejada (1/ 2/ 3): "))

    # Validador das bolas de sorvete
    if bolas not in [1, 2, 3]:
        print("Quantidade de Bolas de Sorvete Inválida.")
        # I. Pedido com número de bolas de sorvete inválido
        print(f"Pedido inválido: sabor({sabor}) bolas({bolas})")
        continue

    # Validador do sabor
    if sabor not in ["tr", "pr", "es"]:
        print("Sabor de Sorvete Inválido.")
        # H. Pedido com sabor inválido
        print(f"Pedido inválido: sabor({sabor}) bolas({bolas})")
        continue
    
    # Soma dos valores do pedido
    if sabor == "tr":
        if bolas == 1:
            total += 6
        elif bolas == 2:
            total += 10
        else:
            total += 14
    elif sabor == "pr":
        if bolas == 1:
            total += 7
        elif bolas == 2:
            total += 12
        else:
            total += 17
    else:
        if bolas == 1:
            total += 8
        elif bolas == 2:
            total += 14
        else:
            total += 20

    # Validador do cliente se deseja algo a mais
    opcao = input("Deseja pedir mais alguma coisa? (s - Sim, n - Não): ")
    if opcao != "s":
        break

# Print do valor total
print(f"Valor total do pedido: R$ {total}")
