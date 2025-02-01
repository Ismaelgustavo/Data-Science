quilometragem = float(input("Quantos quilômetros o carro rodou? "))
dias = int(input("Quantos dias ele foi alugado? "))

pago = (quilometragem * 0.15) + (dias * 60)

print(f"O valor do total do aluguel do carro é:R${ pago: .2f} ")