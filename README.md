﻿# conversorMoeda
## Conversor de Moedas

Este é um simples conversor de moedas em Python que utiliza a API **ExchangeRate-API** para obter taxas de câmbio em tempo real.

## 🔧 Requisitos
- Python 3.x instalado
- Biblioteca `requests` instalada
- Chave de API válida do [ExchangeRate-API](https://www.exchangerate-api.com/)

## 📥 Instalação
1. Clone este repositório ou baixe o arquivo.
2. Instale a biblioteca `requests`, se ainda não tiver:
   ```sh
   pip install requests
   ```
3. Obtenha uma chave de API gratuita no site [ExchangeRate-API](https://www.exchangerate-api.com/).

## 🚀 Como Usar
1. Execute o script em Python:
   ```sh
   python conversor.py
   ```
2. Insira o valor que deseja converter.
3. Informe a moeda de origem e a moeda de destino (exemplo: USD, BRL, EUR).
4. O programa retornará o valor convertido baseado na taxa de câmbio atual.

## 📝 Exemplo de Uso
```
Digite o valor a ser convertido: 100
Digite a moeda de origem (ex: USD, BRL, EUR): USD
Digite a moeda de destino: BRL
100.00 USD equivalem a 500.00 BRL (exemplo)
```

## 🛠 Estrutura do Código
- Obtém os dados da API com a chave informada.
- Verifica se a resposta foi bem-sucedida.
- Converte o valor usando a taxa de câmbio correspondente.
- Exibe o resultado formatado.

## 📌 Observações
- Certifique-se de que sua chave de API está ativa e válida.
- Algumas chaves gratuitas podem ter limite de requisições diárias.

## 📄 Licença
Este projeto é de código aberto e está sob a licença MIT.
