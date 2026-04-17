import requests

# Comando abaixo serve para setar a URL do site
url_amazon = "https://www.amazon.com.br/s?k=rtx+5050&i=computers&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1DXZWAH23YIV3&sprefix=rtx+505%2Ccomputers%2C200&ref=nb_sb_noss_2"

# Comando abaixo serve para fazer requisições GET
response = requests.get(url_amazon)

# Abaixo irei verificar o status e acessar os dados (se conseguir acessar)
if response.status_code == 200:
    dados = response.text()   # Este comando converte a resposta da requisição para Python
    print(dados)
else:
    print(f"Erro: {response.status_code}")