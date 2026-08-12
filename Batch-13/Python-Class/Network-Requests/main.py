import requests

resp = requests.get("https://google.com")
# print(resp.text)

with open('google.html', 'w') as f:
    f.write(resp.text)