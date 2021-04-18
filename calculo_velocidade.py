velocidade_cap = int(input("Informe a velocidade capturada: "))
limite_velocidade_via = int(input("Informe a velocidade permitida da via: "))
placa_veiculo = str(input("Informe a placa do veiculo, sem o hifen: "))
velocidade_final = round(int(limite_velocidade_via * velocidade_cap)) / 100.0

if velocidade_cap > limite_velocidade_via:
    if velocidade_final < 20.00:
        print(f'Veiculo {placa_veiculo} - Infracao media - valor: R$ 130,16.')
    elif velocidade_final < 50.00:
        print(f'Veiculo {placa_veiculo} - Infracao grave - valor: R$ 195,23.')
    elif velocidade_final > 51.00:
        print(f'Veiculo {placa_veiculo} - Infracao gravissima - valor: R$ 880,41.')
else:
    print(f'Veiculo {placa_veiculo} - Velocidade dentro do permitido.')