import json

# Load the generated menu items
with open('new_menu_items.json', 'r', encoding='utf-8') as f:
    menu_blocks = json.load(f)

html_output = ""

# 1. SHAKES (Combining all shake related keys)
shake_keys = ['shakes', 'chocolate-shakes', 'cookies-and-dryfruits-shakes', 'fruit-shakes']
shakes_content = ""
for key in shake_keys:
    if key in menu_blocks:
        # Add a sub-header for each shake type inside the main Shakes accordion
        title = key.replace('-', ' ').title()
        shakes_content += f'<h6 class="text-coffee fw-bold border-bottom pb-2 mt-3">{title}</h6>\n'
        shakes_content += menu_blocks[key]

html_output += f'''
            <!-- SHAKES -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#shakes">
                        <span class="me-2">🥤</span> <span data-en="Shakes" data-gu="Shakes">Shakes</span>
                    </button>
                </h2>
                <div id="shakes" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{shakes_content}                    </div>
                </div>
            </div>
'''

# 2. MOCKTAILS (Separate section)
if 'mocktails' in menu_blocks:
    html_output += f'''
            <!-- MOCKTAILS -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#mocktails">
                        <span class="me-2">🍹</span> <span data-en="Mocktails" data-gu="Mocktails">Mocktails</span>
                    </button>
                </h2>
                <div id="mocktails" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{menu_blocks['mocktails']}                    </div>
                </div>
            </div>
'''

# 3. BIRYANI (Extracting VEG BIRYANI from time-pass or creating a new section)
biryani_html = '<div class="menu-item"><span class="item-name"><span class="item-icon">🍚</span><span data-en="VEG BIRYANI" data-gu="VEG BIRYANI">VEG BIRYANI</span></span><span class=\"item-price\">₹199</span></div>'

html_output += f'''
            <!-- BIRYANI -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#biryani">
                        <span class="me-2">🍚</span> <span data-en="Biryani" data-gu="Biryani">Biryani</span>
                    </button>
                </h2>
                <div id="biryani" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{biryani_html}                    </div>
                </div>
            </div>
'''

# 4. KHICHDI (Empty placeholder)
html_output += f'''
            <!-- KHICHDI -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#khichdi">
                        <span class="me-2">🍲</span> <span data-en="Khichdi" data-gu="Khichdi">Khichdi</span>
                    </button>
                </h2>
                <div id="khichdi" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
                        <p class="text-muted text-center">Items coming soon!</p>
                    </div>
                </div>
            </div>
'''

with open('extra_sections.html', 'w', encoding='utf-8') as f_out:
    f_out.write(html_output)

print("HTML saved to extra_sections.html")
