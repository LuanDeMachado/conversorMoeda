import requests

API_KEY = "af60ac50e4d5403eb61064e0"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def converter_moeda(valor, moeda_origem, moeda_destino):
    url = BASE_URL + moeda_origem
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print("Erro ao obter taxas de câmbio.")
        return None
    
    dados = resposta.json()
    if moeda_destino not in dados["conversion_rates"]:
        print("Moeda de destino inválida.")
        return None
    
    taxa = dados["conversion_rates"][moeda_destino]
    valor_convertido = valor * taxa
    return valor_convertido

# Entrada do usuário
valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: USD, BRL, EUR): ").upper()
moeda_destino = input("Digite a moeda de destino: ").upper()

# Conversão e exibição do resultado
resultado = converter_moeda(valor, moeda_origem, moeda_destino)
if resultado is not None:
    print(f"{valor:.2f} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}")
