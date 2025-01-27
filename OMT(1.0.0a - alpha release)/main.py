import requests
import customtkinter as ctk


class FunctionFrame(ctk.CTkFrame):
    def __init__(self, master, title, values, output_textbox):
        super().__init__(master)

        welcome_message = 'Welcome to OMT alpha release 1.0.0a.\nJust select a function from the function selector and execute. If you have some feedback message me on discord (@siubikyt).\nAnyways I hope you have a great experience with the software :D'
        
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.output_textbox = output_textbox

        self.title = ctk.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,10), sticky='ew')

        self.combobox = ctk.CTkComboBox(self, values=values, command=self.combobox_callback)
        self.combobox.grid(row=1, column=0, padx=10, pady=(10,0), sticky='ew')

        self.button = ctk.CTkButton(self, text='Execute', font=('Segoe UI Bold', 16), corner_radius=6, command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=(10,0), sticky='ew')

        self.entry = ctk.CTkEntry(self, placeholder_text='Input item / changelogs you want to see')
        self.entry.grid(row=3, column=0, padx=10, pady=(10,0), sticky='ew', )
        self.entry.grid_remove()

        self.update_output_textbox(welcome_message)
        print('Welcome to OMT alpha release 1.0.0a.\nJust select a function from the function selector and execute. If you have some feedback message me on discord (@siubikyt).\nAnyways I hope you have a great experience with the software :D')


    def combobox_callback(self, selected_value):
        values_requiring_entry = ['viewChangelogs', 'viewItemInfo']

        print(selected_value)
            
        if selected_value in values_requiring_entry:
            self.entry.grid()
        else:
            self.entry.grid_remove()

    def button_callback(self):
            selected_function = self.combobox.get()
            input_data = self.entry.get()
            print(f'Selected Function: {selected_function}')
            self.execute_function(selected_function, input_data)

    def execute_function(self, function_name, input_data):
        values_requiring_entry = ['viewChangelogs', 'viewItemInfo']
        func = FUNCTIONS.get(function_name)
        if func:
            if function_name in values_requiring_entry:
                result = func(input_data)
            else:
                result = func()

            print(result)
            self.update_output_textbox(result)

    def update_output_textbox(self, text):
        self.output_textbox.configure(state='normal')
        self.output_textbox.delete('1.0', 'end')
        self.output_textbox.insert('end', text)
        self.output_textbox.configure(state='disabled')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Oaklands multitool | made by: siubikyt')
        self.geometry('800x500')
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.label_1 = ctk.CTkLabel(self, text='Oaklands multitool', font=('Segoe UI Bold', 30))
        self.label_1.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.label_2 = ctk.CTkLabel(self, text='1.0.0a (Alpha release)', font=('Segoe UI Bold', 16))
        self.label_2.grid(row=4, column=0, padx=20, pady=20, sticky='ew')

        self.textbox_1 = ctk.CTkTextbox(self, width=400, height=300, corner_radius=6, state='disabled')
        self.textbox_1.grid(row=1, column=2, sticky='nsew')
        
        self.function_frame_1 = FunctionFrame(self, title='Function selector', values=['getCurrentRotationItems', 'getStores', 'getPirateShipLocation', 'getChangelogs', 'getLatestChangelogs', 'viewChangelogs', 'viewItems', 'viewItemInfo'], output_textbox=self.textbox_1)
        self.function_frame_1.grid(row=1, column=0, padx=20, pady=20, sticky='nsew', columnspan=1)


store = 'classic-shop'

oaklandsStoreRotationApi = 'https://public-api.typicaldevelopers.com/v1/oaklands/stores'
oaklandsStoreInformationApi = f'https://public-api.typicaldevelopers.com/v1/oaklands/stores/{store}'
oaklandsPirateShipLocationApi = 'https://public-api.typicaldevelopers.com/v1/oaklands/stores/pirate-ship/location'
oaklandsChangelogsApi = 'https://public-api.typicaldevelopers.com/v1/oaklands/changelogs'
oaklandsItemsApi = 'https://public-api.typicaldevelopers.com/v1/oaklands/items'

headers = {
    'accept': 'application/json'
}

def getCurrentRotationItems():
    response_store_data = requests.get(oaklandsStoreInformationApi, headers=headers)

    
    try:

        response_store_data_json = response_store_data.json()
    
        shop_data = response_store_data_json.get('shop_items', [])

        result = []

        if not shop_data:
            print('No shop data was found.')
            return 'No shop data was found.'
        
        if store == 'classic-shop':
            print('\nClassic Store Items:\n')

        for item in shop_data:
            name = item.get('name', 'Unknown')
            
            identifier = item.get('identifier', 'Unknown')
            price = item.get('price', 'Unknown')
            currency = item.get('currency', 'Unknown')
            item_type = item.get('type', 'Unknown')
            description = item.get('description', 'Unknown')


            print(f'\n--> {name}\n')
            print(f'   |-identifier: {identifier}')
            print(f'   |-price: {price}')
            print(f'   |-currency: {currency}')
            print(f'   |-type: {item_type}')
            print(f'   |-description: {description}\n')

            result.append(f'--> {name}\n')
            result.append(f'   |-identifier: {identifier}')
            result.append(f'   |-price: {price}')
            result.append(f'   |-currency: {currency}')
            result.append(f'   |-type: {item_type}')
            result.append(f'   |-description: {description}\n')

        return '\n'.join(result)

            


    except ValueError:
        print('Response is not a valid JSON')
        print(response_store_data.text)


def getStores():
    response_stores = requests.get(oaklandsStoreRotationApi)

    result = []

    try:

        response_stores_json = response_stores.json()

        stores_data = response_stores_json.get('keys', [])

        print()

        for stores in stores_data:
            print(f'--> {stores}')
            result.append(f'--> {stores}')

        return '\n'.join(result)

        print()

        


    except ValueError:
        print('Response is not a valid JSON')
        print(response_stores.text)


def getPirateShipLocation():
    response_pirate_ship_location = requests.get(oaklandsPirateShipLocationApi)

    response_pirate_ship_location_json = response_pirate_ship_location.json()

    reset_time = response_pirate_ship_location_json.get('reset_time')
    current_location = response_pirate_ship_location_json.get('current_location')
    next_location = response_pirate_ship_location_json.get('next_location')

    result = []

    print(f'\n--> Pirate ship data:\n')
    print(f'     |-time till reset: {reset_time}')
    print(f'     |-current location: {current_location}')
    print(f'     |-next location: {next_location}\n')

    result.append(f'--> Pirate ship data:\n')
    result.append(f'     |-time till reset: {reset_time}')
    result.append(f'     |-current location: {current_location}')
    result.append(f'     |-next location: {next_location}\n')

    return '\n'.join(result)



def getChangelogs():
    response_changelogs = requests.get(oaklandsChangelogsApi)

    response_changelogs_json = response_changelogs.json()

    changelogs_data = response_changelogs_json.get('keys', [])

    result = []

    for changelog in changelogs_data:
        print(changelog)
        result.append(changelog)

    
    return '\n'.join(result)
    


def getLatestChangelogs():
    response_changelogs = requests.get(oaklandsChangelogsApi)

    response_changelogs_json = response_changelogs.json()

    changelogs_data = response_changelogs_json.get('keys', [])
    latest_changelogs = changelogs_data[-1]

    result = []

    print()
    print(latest_changelogs)
    print()

    result.append(latest_changelogs)

    return '\n'.join(result)

def viewChangelogs(input_data):
    

    response_changelogs = requests.get(oaklandsChangelogsApi + '/' + input_data)

    response_changelogs_json = response_changelogs.json()

    changelogs_date = response_changelogs_json.get('date', [])
    changelogs_changed = response_changelogs_json.get('changed', [])
    changelogs_added = response_changelogs_json.get('added', [])
    changelogs_fixed = response_changelogs_json.get('fixed', [])

    result = []

    print(f'\nChangelogs date: {changelogs_date}\n')
    result.append(f'Changelogs date: {changelogs_date}\n')

    if changelogs_changed:
        print(f'Changed:')
        result.append(f'Changed:')
        for line in changelogs_changed:
            print(f'--> {line}')
            result.append(f'--> {line}')
    if not changelogs_changed:
        print(f'Nothing changed')
        result.append(f'Nothing changed')


    if changelogs_added:
        print(f'\nAdded:')
        result.append(f'\nAdded:')
        for line in changelogs_added:
            print(f'--> {line}')
            result.append(f'--> {line}')
    if not changelogs_added:
        print(f'\nNothing added')
        result.append(f'\nNothing added')


    if changelogs_fixed:
        print(f'\nFixed:')
        result.append(f'\nFixed:')
        for line in changelogs_fixed:
            print(f'--> {line}')
            result.append(f'--> {line}')
    if not changelogs_fixed:
        print(f'\nNothing fixed')
        result.append(f'\nNothing fixed')

    return '\n'.join(result)


def viewItems():
    response_items = requests.get(oaklandsItemsApi)

    response_items_json = response_items.json()

    items_data = response_items_json.get('keys', [])

    result = []

    print(f'Items:')
    result.append(f'Items:')

    for item in items_data:
        print(f'--> {item}')
        result.append(f'--> {item}')

    print()
    return '\n'.join(result)
    


def viewItemInfo(input_data):
    response_item = requests.get(oaklandsItemsApi + '/' + input_data)

    response_item_json = response_item.json()

    identifier = response_item_json.get('identifier', 'Unknown')
    name = response_item_json.get('name', 'Unknown')
    description = response_item_json.get('description', 'Unknown')
    store_data = response_item_json.get('store', {})
    item_data = response_item_json.get('item', {})

    result = []

    print(f'\nName: {name}\n')
    print(f'\n--> Identifier: {identifier}')
    print(f'\n--> Description: {description}')

    result.append(f'\nName: {name}\n')
    result.append(f'\n--> Identifier: {identifier}')
    result.append(f'\n--> Description: {description}')
    

    print(f'\n--> Store data:')

    result.append(f'\n--> Store data:')

    try:
        if store_data['currency']:
            print(f'\n   |-currency: {store_data['currency']}')
            result.append(f'\n   |-currency: {store_data['currency']}')
    except KeyError:
        print(f'\n   |-currency: Missing data / Invalid data')
        result.append(f'\n   |-currency: Missing data / Invalid data')

    try:
        if store_data['price']:
            print(f'   |-price: {store_data['price']}')
            result.append(f'   |-price: {store_data['price']}')
    except KeyError:
        print(f'   |-price: Missing data / Invalid data')
        result.append(f'   |-price: Missing data / Invalid data')

    try:
        if store_data['type']:
            print(f'   |-type: {store_data['type']}')
            result.append(f'   |-type: {store_data['type']}')
    except KeyError:
        print(f'   |-type: Missing data / Invalid data')
        result.append(f'   |-type: Missing data / Invalid data')

    print(f'\n--> Item data:')
    result.append(f'\n--> Item data:')

    try:
        if item_data['additionalProp1']:
            print(f'\n   |-additionalProp1: {item_data['additionalProp1']}')
            result.append(f'\n   |-additionalProp1: {item_data['additionalProp1']}')
    except KeyError:
        print(f'\n   |-additionalProp1: Missing data / Invalid data')
        result.append(f'\n   |-additionalProp1: Missing data / Invalid data')

    try:
        if item_data['additionalProp2']:
            print(f'   |-additionalProp2: {item_data['additionalProp2']}')
            result.append(f'   |-additionalProp2: {item_data['additionalProp2']}') 
    except KeyError:
        print(f'   |-additionalProp2: Missing data / Invalid data')
        result.append(f'   |-additionalProp2: Missing data / Invalid data')

    try:
        if item_data['additionalProp3']:
            print(f'   |-additionalProp3: {item_data['additionalProp3']}')
            result.append(f'   |-additionalProp3: {item_data['additionalProp3']}')
    except KeyError:
        print(f'   |-additionalProp3: Missing data / Invalid data')
        result.append(f'   |-additionalProp3: Missing data / Invalid data')

    return '\n'.join(result)


def functionToTextbox():
    com = FunctionFrame.button_callback()

    if com == 'getCurrentRotationItems':
        getCurrentRotationItems()

    elif com == 'getStores':
        getStores()

    elif com == 'getPirateShipLocation':
        getPirateShipLocation()

    elif com == 'getChangelogs':
        getChangelogs()

    elif com == 'getLatestChangelogs':
        getLatestChangelogs()

    elif com == 'viewChangelogs':
        viewChangelogs()

    elif com == 'viewItems':
        viewItems()

    elif com == 'viewItemInfo':
        viewItemInfo()

    else:
        print('\nFunction could not be found or is invalid.\n')     


FUNCTIONS = {
    "getCurrentRotationItems": getCurrentRotationItems,
    "getStores": getStores,
    "getPirateShipLocation": getPirateShipLocation,
    "getChangelogs": getChangelogs,
    "getLatestChangelogs": getLatestChangelogs,
    "viewChangelogs": viewChangelogs,
    "viewItems": viewItems,
    "viewItemInfo": viewItemInfo,
}


app = App()
app.mainloop()