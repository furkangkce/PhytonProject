import requests

baseurl="https://pokeapi.co/api/v2/"

def get_info(name):
    url=f"{baseurl}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("SUCCESS")
        return response.json()
    else:
        print(f"Error {response.status_code}")
        return None

name="typhlosion"
info1 = get_info(name)

if info1:
    print(f"Name {info1["name"]}")
    print(f"Id {info1["id"]}")
    print(f"Height {info1['height']}")
