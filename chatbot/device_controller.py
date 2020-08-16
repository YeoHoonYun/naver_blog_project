import time
import requests

url = "http://192.168.0.104:8123/api/services/light/turn_on"

payload = "{ \n\t\"entity_id\" : \"light.living_room\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NzY3YjJiNTQzMzc0MDAxYTg5YzUxMGY5ZjkzOTA5OSIsImlhdCI6MTU5NTk0MDY0MiwiZXhwIjoxOTExMzAwNjQyfQ.YabgBIupXkI5AV-1pSj4WtUS94YoOG_XzS6ysK50kGA'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

time.sleep(2)

url = "http://192.168.0.104:8123/api/services/light/turn_off"

payload = "{ \n\t\"entity_id\" : \"light.living_room\"\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI0NzY3YjJiNTQzMzc0MDAxYTg5YzUxMGY5ZjkzOTA5OSIsImlhdCI6MTU5NTk0MDY0MiwiZXhwIjoxOTExMzAwNjQyfQ.YabgBIupXkI5AV-1pSj4WtUS94YoOG_XzS6ysK50kGA'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
