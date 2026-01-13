import json

# Load the generated menu items
with open('new_menu_items.json', 'r', encoding='utf-8') as f:
    menu_blocks = json.load(f)

# Define category display names and emojis
category_info = {
    'noodles': ('Noodles', '🍜'),
    'breads': ('FOI Breads (Garlic Breads)', '🥖'),
    'cold-coffee': ('Cold Coffee', '☕'),
    'hot-coffee': ('Hot Coffee', '☕'),
    'tea': ('Tea', '🍵'),
    'ice-tea': ('Ice Tea', '🍵'),
    'sweet-corn': ('Sweet Corn', '🌽'),
    'french-fries': ('French Fries', '🍟'),
    'quick-bites': ('Quick Bites', '🥯'),
    'chocolate-shots': ('Chocolate Shots', '⚪'),
    'shakes': ('Shakes', '🥤'),
    'chocolate-shakes': ('Chocolate Shakes', '🥤'),
    'cookies-and-dryfruits-shakes': ('Cookies & Dryfruits Shakes', '🥤'),
    'fruit-shakes': ('Fruit Shakes', '🥤'),
    'chinese-menu': ('Chinese Menu', '🥢'),
    'starters': ("Starter's", '✨'),
    'pav-bhaji': ('Pav Bhaji', '🥘'),
    'sandwiches': ('Sandwiches', '🥪'),
    'momos': ('Momos', '🥟'),
    'soya-chaaps': ('Soya Chaaps', '🍖'),
    'pizza': ('Pizza Hub', '🍕'),
    'mocktails': ('Mocktails', '🍹'),
    'rolls': ('Rolls', '🌯'),
    'burger': ('Burgers', '🍔'),
    'pasta': ('Pasta', '🍝'),
    'new-arrivals': ('New Arrivals', '✨'),
    'vada-pav': ('Vada Pav', '🥯'),
    'time-pass': ('Time Pass', '🍿')
}

# Generate accordion items
accordion_html = ""
first = True
for cat_id, (cat_name, emoji) in category_info.items():
    if cat_id in menu_blocks:
        collapse_class = "show" if first else ""
        button_class = "" if first else " collapsed"
        first = False
        
        accordion_html += f'''
            <!-- {cat_name.upper()} -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button{button_class}" type="button" data-bs-toggle="collapse" data-bs-target="#{cat_id}">
                        <span class="me-2">{emoji}</span> <span data-en="{cat_name}" data-gu="{cat_name}">{cat_name}</span>
                    </button>
                </h2>
                <div id="{cat_id}" class="accordion-collapse collapse {collapse_class}" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{menu_blocks[cat_id]}                    </div>
                </div>
            </div>
'''

# Save to file
with open('accordion_sections.html', 'w', encoding='utf-8') as f:
    f.write(accordion_html)

print(f"Generated accordion HTML with {len(category_info)} sections")
print("Saved to: accordion_sections.html")
