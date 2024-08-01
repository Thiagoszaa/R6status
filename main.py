import requests

def pegar_status_player (username, platform= 'uplay' ):
    api_key = 'Sua-key'
    url = f'https://public-api.tracker.gg/v2/rainbow-six/{platform}/profile/{platform}/{username}/segments/season'

    headers = {
        'TRN-API-KEY': api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']

    else:
        print(f"Error: {response.status_code}")
        return None

def print_rank (rank_data):
    if rank_data:
        for season in rank_data:
            print(f"Season: {season['season']}")
            print(f"Rank: {season['stats']['rank']['metadata']['rankName']}")
            print(f"Rank Image: {season['stats']['rank']['metadata']['iconUrl']}\n")
    else:
        print("Não foi possivel achar conta.")

username = input("Digite o nick do jogador: ")
platform = 'uplay'  # Pode ser 'uplay', 'psn', ou 'xbl'
rank_data = pegar_status_player(username, platform)
pegar_status_player(rank_data)
