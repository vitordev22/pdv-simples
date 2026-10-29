contador = 0
compras = []
totalBruto = 0
totalDescontos = 0
totalFinal = 0

while(True):
    
    valorCompra = float(input("Informe o valor da compra: "))
    if valorCompra == 0:
        break
    idadeCliente = int(input("Informe a idade do cliente: "))
    # Validação de entrada
    if valorCompra < 0 or idadeCliente < 0:
        print("Error! Insira valores válidos. ")
        continue
    
    valorDesconto = 0
    valorFinal = valorCompra

    # Desconto por idade
    if idadeCliente >= 65: 
        valorDesconto = valorCompra*0.2
        valorFinal = valorCompra - valorDesconto

        totalDescontos += valorDesconto # incrementa no total de descontos
        # Desconto extra
        if valorFinal > 100:
            valorDesconto = 0
            valorDesconto = valorFinal*0.1
            valorFinal -= valorDesconto
            totalDescontos += valorDesconto #incrementa no total de descontos

    
    #Desconto por valor
    if idadeCliente < 65 and valorFinal > 100:
        valorDesconto = 0
        valorDesconto = valorFinal*0.1
        valorFinal -= valorDesconto
        totalDescontos += valorDesconto #incrementa no total de descontos

    
    #incrementos para o resumo diário
    compras.append(valorFinal)
    contador += 1
    totalBruto += valorCompra
    totalFinal += valorFinal
    
    
    print(f"Valor final: R$ {valorFinal:.2f}")
    print()

print("")
print("------------ RESUMO DO DIA -------------")
print(f"Quantidade de vendas registradas: {contador}")
print(f"Total bruto: R$ {totalBruto:.2f}")
print(f"Total de descontos concedidos: R$ {totalDescontos:.2f}")
print(f"Total final: R$ {totalFinal:.2f}")
