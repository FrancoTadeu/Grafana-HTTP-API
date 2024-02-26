import requests
import json
import sys

url = "http://localhost:3000/api/teams"

empresa = sys.argv[1]
token = "eyJrIjoicUF3NUczZUg1Q3pSeU1wcDNUN1pwb2hyVDhpdlNJNWciLCJuIjoiR3JhZmFuYSBBUEkgVGVzdGVzIiwiaWQiOjF9"
#
# Criação do time de Viewer
#
payload_team = json.dumps({
    "name": f"{empresa} Viewer",
    "email": f"{empresa}@grafana.com",
    "orgId": 1
})
headers_team = {
  'Content-Type': 'application/json',
  'Authorization': f"Bearer {token}"
}

response_team = requests.request("POST", url=url, headers=headers_team, data=payload_team)
print(response_team.text)

try:
    response_team_id = response_team.json()
    team_empresa_id = response_team_id.get('teamId') # Correção, no caso do Team não se utiliza id, mas teamId
    if team_empresa_id:
        print(f"Id for Team '{empresa} Viewer' is {team_empresa_id}")
    else:
        print("Error extracting Team ID from response.")
except json.JSONDecodeError:
    print("Error decoding JSON response.")
    print(response_team.text)