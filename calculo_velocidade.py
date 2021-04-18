velocidade_cap = int(input("Informe a velocidade capturada: "))
limite_velocidade_via = int(input("Informe a velocidade permitida da via: "))
placa_veiculo = str(input("Informe a placa do veiculo: "))
velocidade_final = round(int(limite_velocidade_via * velocidade_cap)) / 100.0

if velocidade_cap > limite_velocidade_via:
    if velocidade_final < 20.00:
        print(f'{placa_veiculo} - {velocidade_cap} km/h - Media R$ 130,16.')
    elif velocidade_final < 50.00:
        print(f'{placa_veiculo} - {velocidade_cap} km/h- Grave R$ 195,23.')
    elif velocidade_final > 51.00:
        print(f'{placa_veiculo} - {velocidade_cap} km/h - Gravissima R$ 880,41.')
else:
    print(f'Veiculo {placa_veiculo} - {velocidade_cap} km/h - Permitido.')