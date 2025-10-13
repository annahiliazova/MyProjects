import requests
from textwrap import fill

base_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/"
summary_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"


def fetch_champion_summary():
    try:
        response = requests.get(summary_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch champion list: HTTP {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return []


def get_champion_id(name):
    champions = fetch_champion_summary()
    for champ in champions:
        if champ["name"].lower() == name.lower():
            return champ["id"]
    return None


def get_champion_info(name):
    champ_id = get_champion_id(name)
    if champ_id is None:
        print(f"Champion '{name}' not found.")
        return

    url = f"{base_url}{champ_id}.json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to load champion data: HTTP {response.status_code}")
            return

        data = response.json()
        print(f"\n{data['name']}")
        print(f"Title: {data['title']}")
        bio = data["shortBio"]
        print(fill(bio, width=80))

        print("\nSpells:")
        for spell in data["spells"]:
            key = spell["spellKey"].upper()
            spell_name = spell["name"]
            desc = spell["description"]
            print(f"\n  [{key}] {spell_name}")
            print(fill(desc, width=75, initial_indent="    ", subsequent_indent="    "))
    except requests.RequestException as e:
        print(f"Network error while loading champion: {e}")
    except KeyError as e:
        print(f"Unexpected data format (missing key: {e})")


if __name__ == "__main__":
    champ_name = input("Enter champion name: ").strip()
    if champ_name:
        get_champion_info(champ_name)
    else:
        print("No name provided.")
