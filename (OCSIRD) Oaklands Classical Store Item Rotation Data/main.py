import requests

store = 'classic-shop'

oaklandsStoreRotationApi = 'https://public-api.typicaldevelopers.com/v1/oaklands/stores'
oaklandsStoreInformationApi = f'https://public-api.typicaldevelopers.com/v1/oaklands/stores/{store}'
headers = {
    'accept': 'application/json'
}

def getCurrentRotationItems():
    response = requests.get(oaklandsStoreRotationApi, headers=headers)
    response_store_data = requests.get(oaklandsStoreInformationApi, headers=headers)

    
    try:
        response_json = response.json()

        response_store_data_json = response_store_data.json()
        
        store_keys = response_json.get('keys', [])
        shop_data = response_store_data_json.get('shop_items', [])
        
        
        if not store_keys:
            print('No store keys found in the response.')
            return
        
        print('\nClassic Store Items:\n')

        for item in shop_data:
            name = item.get('name', 'Unknown')
            
            identifier = item.get('identifier', 'Unknown')
            price = item.get('price', 'Unknown')
            currency = item.get('currency', 'Unknown')
            item_type = item.get('type', 'Unknown')


            print(f'\n--> {name}\n')
            print(f'   -identifier: {identifier}')
            print(f'   -price: {price}')
            print(f'   -currency: {currency}')
            print(f'   -type: {item_type}\n')


    except ValueError:
        print('Response is not a valid JSON')
        print(response.text)


getCurrentRotationItems()