import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
seed = "12345"

while True:
    seed = requests.get(url + seed).text.split()[-1]
    print(seed)
