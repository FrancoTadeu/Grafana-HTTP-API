import requests
import json
import socket # Obter endereço IP da máquina que executa o script (Deve ser executado do Host do Grafana OSS)
import platform # Determina a plataforma (Se é Unix ou Windows)
import sys

"""FALTA
- Adicionar o usuário telictec também de visualização
- Adicionar o gerador de senhas randomicas para cada user
- Adicionar os dois usuários aos Time gerado 

- Cada um dos user ou team quando criado
gera um id unico que deve ser obtido para uso nos passos seguintes
"""

empresa = sys.argv[1]
token = sys.argv[2]
# Obtém o endereço IP do host
host_ip = socket.gethostbyname(socket.gethostname())

# Determine the Grafana URL based on the operating system
if platform.system() == "Windows":
    grafana_url = f"http://{host_ip}:3000"
else:
    grafana_url = f"http://{host_ip}:3000"

url = f"{grafana_url}/api/admin/users"
url_team = f"{grafana_url}/api/teams"


# #
# Criação do usuário Telic telictec
# #
payload_user_telictec = json.dumps({
  "name": f"telictec Viewer",
  "email": f"telictec@telic.com.br",
  "login": f"telictec",
  "password": "Sp!derm4n",
  "orgId": 1,
  "isDisabled": False
})
headers_user_tel = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response_user_telictec = requests.request("POST", url, headers=headers_user_tel, data=payload_user_telictec)

try:
    response_user_id_telictec = response_user_telictec.json()
    user_telictec_id = response_user_id_telictec.get('id') # Para user se utiliza id
    if user_telictec_id is not None:
        print(f"Id for user 'telictec' is {user_telictec_id}")
    else:
        print("Error extracting user ID from response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
    #print(response_user.text)

# #
# Criação do usuário para a Empresa contratante
# #
payload_user = json.dumps({
  "name": f"{empresa}",
  "email": f"{empresa}@example.com",
  "login": f"{empresa}",
  "password": "empresa_tec2",
  "orgId": 1,
  "isDisabled": False
})
headers_user = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response_user = requests.request("POST", url, headers=headers_user, data=payload_user)

try:
    response_user_id = response_user.json()
    user_empresa_id = response_user_id.get('id') # Para user se utiliza id
    if user_empresa_id is not None:
        print(f"Id for user '{empresa}' is {user_empresa_id}")
    else:
        print("Error extracting user ID from response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
    #print(response_user.text)


# #
# Criação do time de Viewer
# #
payload_team = json.dumps({
    "name": f"{empresa} Viewer",
    "email": f"{empresa}@grafana.com",
    "orgId": 1
})
headers_team = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {token}"
}

response_team = requests.request("POST", url_team, headers=headers_team, data=payload_team)

try:
    response_team_id = response_team.json()
    team_empresa_id = response_team_id.get('teamId') # Correção, no caso do Team não se utiliza id, mas teamId
    if team_empresa_id:
        print(f"Id for Team '{empresa} Viewer' is {team_empresa_id}")
    else:
        print("Error extracting Team ID from response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
    #print(response_team.text)

# 
# Adicionar os usuários criados ao time 
#
all_user_id = [user_telictec_id, user_empresa_id]
#print(all_user_id)

for uid in all_user_id:
    team_add_url = f"{grafana_url}/api/teams/{team_empresa_id}/members"
    data_uid = f'{{"UserId": {uid}}}'
    headers_final_team = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46YWRtaW4='
        }
    request_final = requests.request("POST", url=team_add_url, headers=headers_final_team, data=data_uid)
    print(request_final.text)