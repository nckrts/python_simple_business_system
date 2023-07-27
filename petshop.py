 
print("Bem-vindo ao petshop do Nicolas Romancini Tarouco Silveira!")

pesoCachorro = 0
# Recebe o peso do cachorro
def cachorro_peso():
    while True:
        try:
            pesoCachorro = peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 0:
                raise ValueError
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Desculpe, não aceitamos cachorro tão grande.")
        except ValueError:
            print("Você digitou um valor não numérico.")
            print("Por favor, entre com o pesodo cachorro nomavamente.")

# Pega o pelo do cachorro
def cachorro_pelo():
    while True:
        print("Digite o tipo de pelo do cachorro:")
        print("c - curto")
        print("m - médio")
        print("l - longo")
        pelo = input("Digite o número da opção desejada: ")
        if pelo in ['c', 'm', 'l']:
            if pelo == 'c':
                return 1
            elif pelo == 'm':
                return 1.5
            elif pelo == 'l':
                return 2
        else:
            print("Por favor, digite uma opção válida para o tipo de pelo.")

# Pega as opões extras
def cachorro_extra():
    extras = 0
    while True:
        print("Selecione um serviço adicional:")
        print("1. Cortar unhas (R$10)")
        print("2. Escovar dentes (R$12)")
        print("3. Limpar orelhas (R$15)")
        print("0. Não querer mais nada")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == '1':
            extras += 10
        elif opcao == '2':
            extras += 12
        elif opcao == '3':
            extras += 15
        elif opcao == '0':
            return extras
        else:
            print("Por favor, digite um número válido para a opção.")

# Total
try:
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()
    total = base * multiplicador + extra
    print(f"Total a pagar: R$ {total} (peso: {pesoCachorro} * pelo: {multiplicador} + adicionais: {extra})")
except ValueError:
    print("Por favor, digite um valor numérico válido para o peso.")
