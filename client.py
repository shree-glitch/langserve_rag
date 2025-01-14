import requests

response = requests.post(
    "http://localhost:8000/essay/invoke",
    json = {"input": {"topic": "Large Language Models"}})

try:
    print(response.json()[0][0])
except Exception as e:
    print(e.msg, e.doc, e.pos)