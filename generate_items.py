
import json

with open(r'C:\Users\Administrator\Downloads\report_decode\FOI_menu\menu_data.json', 'r') as f:
    data = json.load(f)

def get_icon(name):
    name = name.lower()
    if 'maggi' in name: return '🍜'
    if 'garlic bread' in name: return '🥖'
    if 'coffee' in name: return '☕'
    if 'tea' in name: return '🍵'
    if 'corn' in name: return '🌽'
    if 'fries' in name: return '🍟'
    if 'chinese' in name or 'noodle' in name or 'rice' in name: return '🥢'
    if 'sandwich' in name: return '🥪'
    if 'momo' in name: return '🥟'
    if 'chaap' in name: return '🍖'
    if 'pizza' in name: return '🍕'
    if 'mocktail' in name or 'mojito' in name or 'cooler' in name or 'lemonade' in name: return '🍹'
    if 'shake' in name: return '🥤'
    if 'roll' in name: return '🌯'
    if 'burger' in name: return '🍔'
    if 'pasta' in name: return '🍝'
    if 'pav bhaji' in name: return '🥘'
    if 'vada pav' in name: return '🥯'
    if 'nuggets' in name or 'bites' in name or 'shot' in name: return '⚪'
    return '✨'

def format_item(item):
    name = item.get('ITEMS NAME')
    price = item.get('FINAL RATE')
    if not name or price is None: return ""
    icon = get_icon(name)
    return f'                        <div class="menu-item"><span class="item-name"><span class="item-icon">{icon}</span><span data-en="{name}" data-gu="{name}">{name}</span></span><span class="item-price">₹{int(price)}</span></div>\n'

categories = {}
current_cat = "Other"

for item in data:
    name = item.get('ITEMS NAME')
    if name and item.get('FINAL RATE') is None:
        current_cat = name.upper()
        categories[current_cat] = []
    elif name and item.get('FINAL RATE') is not None:
        if current_cat not in categories: categories[current_cat] = []
        categories[current_cat].append(item)

# Mapping to HTML IDs
mapping = {
    'NOODLES': 'maggi',
    'MAGGI': 'maggi',
    'BREADS': 'garlic-bread',
    'COLD COFFEE': 'coffee',
    'HOT COFFEE': 'coffee',
    'TEA': 'coffee',
    'ICE TEA': 'coffee',
    'SWEET CORN': 'fries',
    'FRENCH FRIES': 'fries',
    'CHINESE MENU': 'chinese',
    'STARTER\'S': 'chinese',
    'PAV BHAJI': 'pav-bhaji',
    'SANDWICHES': 'sandwiches',
    'MOMO\'S': 'momos',
    'SOYA CHAAPS': 'soya',
    'PIZZA': 'pizza',
    'MOCKTAILS': 'beverages',
    'SHAKES': 'beverages',
    'CHOCOLATE SHAKES': 'beverages',
    'COOKIES & DRYFRUITS SHAKES': 'beverages',
    'FRUIT SHAKES': 'beverages',
    'ROLLS': 'others',
    'BURGER': 'others',
    'PASTA': 'others',
    'VADA PAV': 'vada-pav',
    'TIME PASS': 'time-pass',
    'NEW ARRIVALS': 'quick-bites',
    'VEG BIRYANI': 'khichdi'
}

# Generate blocks
html_blocks = {}
for cat, items in categories.items():
    html_id = mapping.get(cat, 'others')
    if html_id not in html_blocks: html_blocks[html_id] = ""
    
    # Add subheader if it's a grouped section
    if cat in ['COLD COFFEE', 'HOT COFFEE', 'TEA', 'ICE TEA', 'SHAKES', 'CHOCOLATE SHAKES', 'FRUIT SHAKES', 'COOKIES & DRYFRUITS SHAKES', 'TIME PASS']:
         html_blocks[html_id] += f'                        <h6 class="text-coffee fw-bold border-bottom pb-2 mt-3">{cat.title()}</h6>\n'
    
    for item in items:
        html_blocks[html_id] += format_item(item)

with open(r'C:\Users\Administrator\Downloads\report_decode\FOI_menu\new_menu_items.json', 'w') as out:
    json.dump(html_blocks, out, indent=2)
