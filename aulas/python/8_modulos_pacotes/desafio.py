# 🔹 DESAFIO: Explorando Informações do IBGE 🌍

# 📌 Enunciado:
# O Instituto Brasileiro de Geografia e Estatística (IBGE) disponibiliza diversas APIs abertas para consulta de dados.
# Neste desafio, você deve criar um programa que consulta a API de **Localidades** do IBGE para obter informações sobre estados brasileiros.
# O sistema deve funcionar da seguinte forma:
# 1. O usuário deve inserir o nome ou código do estado.
# 2. O programa deve buscar os dados desse estado na API do IBGE.
# 3. Exibir as seguintes informações:
#    - Nome do estado
#    - Sigla do estado
#    - Região à qual pertence
# 4. Pergunte ao usuário se deseja consultar outro estado. Caso contrário, finalize o programa.

# ✅ Tarefa:
# - Criar uma função chamada `consultar_estado(estado)` que faz a requisição para a API do IBGE.
# - Utilizar o pacote externo `requests` para fazer a requisição HTTP. 
# Caso não possua instalar utilizando o comando `pip install requests`.
# - Processar a resposta JSON utilizando a biblioteca `json`.
# - Permitir múltiplas consultas até o usuário digitar "sair".

# 🔥 Dica:
# - A API de Localidades do IBGE pode ser consultada no seguinte endpoint:
#   `https://servicodados.ibge.gov.br/api/v1/localidades/estados`
# - Utilize `json()` para processar a resposta da API.
# - Trate possíveis erros, como estado não encontrado ou falha na conexão.

# ✏️ Comece seu código abaixo: