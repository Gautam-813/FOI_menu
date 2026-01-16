import json

# Load the generated menu items
with open('new_menu_items.json', 'r', encoding='utf-8') as f:
    menu_blocks = json.load(f)

# Define the new separated categories
target_categories = [
    # ID in JSON,  Display Name, Emoji, HTML ID
    ('quick-bites', 'Quick Bites', '🥯', 'quick-bites'),
    ('chocolate-shots', 'Chocolate Shots', '⚪', 'chocolate-shots'),
    ('rolls', 'Rolls', '🌯', 'rolls'),
    ('burger', 'Burgers', '🍔', 'burgers'),
    ('pasta', 'Pasta', '🍝', 'pasta')
]

html_output = ""

for json_key, title, emoji, html_id in target_categories:
    if json_key in menu_blocks:
        content = menu_blocks[json_key]
        html_output += f'''
            <!-- {title.upper()} -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{html_id}">
                        <span class="me-2">{emoji}</span> <span data-en="{title}" data-gu="{title}">{title}</span>
                    </button>
                </h2>
                <div id="{html_id}" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{content}                    </div>
                </div>
            </div>
'''

print(html_output)
