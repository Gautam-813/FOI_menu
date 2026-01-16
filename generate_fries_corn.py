import json

# Read the generated menu items
with open('c:/Users/Administrator/Downloads/report_decode/FOI_menu/new_menu_items.json', 'r', encoding='utf-8') as f:
    menu_blocks = json.load(f)

html_output = ""

# Generate Sweet Corn Section
if 'sweet-corn' in menu_blocks:
    html_output += f'''
            <!-- SWEET CORN -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sweet-corn">
                        <span class="me-2">🌽</span> <span data-en="Sweet Corn" data-gu="Sweet Corn">Sweet Corn</span>
                    </button>
                </h2>
                <div id="sweet-corn" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{menu_blocks['sweet-corn']}
                    </div>
                </div>
            </div>
'''

# Generate French Fries Section
if 'french-fries' in menu_blocks:
    html_output += f'''
            <!-- FRENCH FRIES -->
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#french-fries">
                        <span class="me-2">🍟</span> <span data-en="French Fries" data-gu="French Fries">French Fries</span>
                    </button>
                </h2>
                <div id="french-fries" class="accordion-collapse collapse" data-bs-parent="#menuAccordion">
                    <div class="accordion-body">
{menu_blocks['french-fries']}
                    </div>
                </div>
            </div>
'''

# Write to file to avoid unicode errors in console
with open('c:/Users/Administrator/Downloads/report_decode/FOI_menu/fries_corn.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("Generated HTML written to fries_corn.html")
