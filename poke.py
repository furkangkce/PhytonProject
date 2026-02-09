import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_info(name):
    url = BASE_URL + name.lower()
    response = requests.get(url)

    if response.status_code != 200:
        print("Pokemon bulunamadı!")
        return None

    data = response.json()

    pokemon_info = {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    }

    return pokemon_info


pokemon_name = input("Pokemon adı gir: ")
info = get_pokemon_info(pokemon_name)

if info:
    print("\n--- Pokemon Bilgileri ---")
    print("İsim:", info["name"])
    print("Boy:", info["height"])
    print("Kilo:", info["weight"])
    print("Türler:", ", ".join(info["types"]))
    print("Yetenekler:", ", ".join(info["abilities"]))

    print("\nİstatistikler:")
    for stat, value in info["stats"].items():
        print(f"{stat}: {value}")
