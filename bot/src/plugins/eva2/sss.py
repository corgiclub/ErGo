import requests
import json

url = "http://i.tech.corgi.plus:6666/api/inference"

payload = json.dumps({
  "query_context": [
    "ddd",
    "sss"
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, proxies=None)

print(response.text)
print(response.status_code)
print(payload)
