import requests

parameters = {
    "amount": 10,
    "type": "boolean",

}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.status_code

question_data = response.json()["results"]
