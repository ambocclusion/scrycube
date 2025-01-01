import requests, json, urllib.parse

commonAmount = input('common count: ')
uncommonAmount = input('uncommon count: ')
rareAmount = input('rare count: ')
mythicAmount = input('mythic count: ')
set = input('set')

query = f'set={set}'
url = f'https://api.scryfall.com/cards/search?order=rarity&q={urllib.parse.quote(query)}'

print(url)
count = 0
while True:
    request = requests.get(url)

    j = json.loads(request.content)

    for d in j['data']:
        if 'basic' in d['type_line'].lower():
            continue
        name = d['name']
        collector_number = d['collector_number']

        if d['layout'] == 'adventure':
            name = d['card_faces'][0]['name']

        if d['rarity'] == 'common':
            print(f'{commonAmount} {name} [{set}] {collector_number}')
        if d['rarity'] == 'uncommon':
            print(f'{uncommonAmount} {name} [{set}] {collector_number}')
        if d['rarity'] == 'rare':
            print(f'{rareAmount} {name} [{set}] {collector_number}')
        if d['rarity'] == 'mythic':
            print(f'{mythicAmount} {name} [{set}] {collector_number}')
        count+=1

    if j['has_more'] == True:
        url = j['next_page']
    else:
        print(str(count))
        break