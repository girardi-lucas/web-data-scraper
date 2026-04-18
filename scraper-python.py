import requests

# Comando de ativação do venv : .\venv\Scripts\Activate.ps1

# Criando a mascara de acesso:
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

# Comando abaixo serve para setar a URL do site
url_test = "http://books.toscrape.com/"

# Comando abaixo serve para fazer requisições GET (adicionei o header para realizar o get)
response = requests.get(url_test, headers=headers)

# Abaixo irei verificar o status e acessar os dados (se conseguir acessar)
if response.status_code == 200:
    dados = response.text   # Este comando converte a resposta da requisição para Python
    print(dados)
    print(len(dados))
else:
    print(f"Erro: {response.status_code}")