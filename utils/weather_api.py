import http.client
import json

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7065d0b603msh3e67a3809ccd1adp15f04ajsn0af2c662e4eb",
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
    }

def temp_humid(district: str, state: str):
    district = district.replace(' ', '_')
    state = state.replace(' ', '_')
    conn.request("GET", f"/current.json?q={district},{state}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    data = data.decode("utf-8")
    s = json.loads(data)
    temperature = s["current"]["temp_c"]
    humidity = s["current"]["humidity"]
    return temperature, humidity