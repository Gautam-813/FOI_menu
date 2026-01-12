
import json

with open(r'C:\Users\Administrator\Downloads\report_decode\FOI_menu\menu_data.json', 'r') as f:
    data = json.load(f)

for item in data:
    if item.get('FINAL RATE') is None and item.get('ITEMS NAME'):
        print(item.get('ITEMS NAME'))
