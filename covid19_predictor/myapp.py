import json
import requests
URL = "http://127.0.0.1:8000/api/"

def covid_predictor():
    data = {"cough":1, "fever":1, "breath": 1, "age":22, "environment":1, "hypertension":1, "diabetes":1, "cardiovascular":1, "respiratory":1, "immune":1}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.post(url = URL, data = json_data)
    print("hahahahahahah")
    print(r.json())
covid_predictor()