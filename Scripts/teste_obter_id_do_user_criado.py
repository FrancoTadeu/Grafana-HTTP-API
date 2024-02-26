import requests
import json

url = "http://localhost:3000/api/admin/users"

payload = {'name': 'teste2 Geral',
'email': 'teste2@grafana.com',
'login': 'teste2',
'orgId': '1',
'isDisabled': 'False',
'password': 'alguma_coisa'}
files=[

]
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

# OBTER USER ID CORRETO
# Utilizar este mesma lógica para o Grafana Team
try:
    response_data = response.json()
    user_id = response_data.get('id')
    if user_id is not None:
        print(f"{user_id}")
    else:
        print("Error extracting user ID from response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
    print(response.text)

# user_id = json.loads(response.text).get('id', None)

# if user_id is not None:
#     print({user_id})
# else:
#     print("Error creating user.")

#print(response.text)


