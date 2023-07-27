# Print de bem vindo
print("Bem vindo a loja do Nicolas Romancini Tarouco Silveira!")

# Valor e quantidade do produto
valorProduto = float(input("Entre com o valor do produto: "))
quantidadeProduto = int(input("Enter com a quantidade do produto: "))

# Calculando o total de disconto
totalSemDesconto = valorProduto * quantidadeProduto

# Aplica o desconto
if quantidadeProduto < 200:
    desconto = 0
elif quantidadeProduto < 1000:
    desconto = 5
elif quantidadeProduto < 2000:
    desconto = 10
else:
    desconto = 15

# Calcula o desconto do produto
descontoTotal = totalSemDesconto * (desconto / 100)
TotalFinalcomDesconto = totalSemDesconto - descontoTotal

# Print com os valores
print("Valor sem desconto: R$", totalSemDesconto)
print("Valor com desconto: R$", TotalFinalcomDesconto)
