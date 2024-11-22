import requests

api_url = "https://api.clearsky.services/api/v1/anon/get-list/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def get_starter_packs(username, retries=10):
    response = requests.get(api_url + username, headers=headers)

    tries = 0
    while tries < retries:
        if response.status_code == 200:
            break
        else:
            response = requests.get(api_url + username, headers=headers)
            tries += 1

    if response.status_code != 200:
        return None

    lists = response.json()['data']['lists']
    return [dict(name=l['name'], description=l['description'], handle=l['handle'], url=l['url']) for l in lists]


if __name__ == "__main__":
    username = ["cgprograms.com", "steelwolfstudios.com"]

    while not username:
        username = input("Enter your username(s): ")

    if type(username) == list:
        usernames = username
    elif "," in username:
        usernames = username.split(",")
    else:
        usernames = [username]

    for user in usernames:
        user = user.strip()
        print(f"\nStarter Packs for {user}:")
        starter_packs = get_starter_packs(user)
        if starter_packs is None:
            print("Failed to get starter packs.")
        elif not starter_packs:
            print("No starter packs found.")
        else:
            for pack in starter_packs:
                print(pack)
