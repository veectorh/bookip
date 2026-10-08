import re

# index.html
with open('index.html', 'r') as f:
    content = f.read()

# Replace desktop rows in index
desktop_rows = """                        {{> editor-item-desktop name="Website retainer" tax="VAT 7.5%" qty="1" price="150,000.00" amount="161,250.00" }}
                        {{> editor-item-desktop name="Hosting — 12 months" tax="None" qty="1" price="45,000.00" amount="45,000.00" }}"""
content = re.sub(r'<tr>.*?161,250.00.*?</tr>.*?<tr>.*?45,000.00.*?</tr>', desktop_rows, content, flags=re.DOTALL)

# Replace mobile cards in index
mobile_cards = """                    {{> editor-item-mobile name="Website retainer" tax="VAT 7.5%" qty="1" price="150,000.00" amount="161,250.00" }}
                    {{> editor-item-mobile name="Hosting — 12 months" tax="None" qty="1" price="45,000.00" amount="45,000.00" }}"""
content = re.sub(r'<div class="flex flex-col border border-line-strong rounded p-3 bg-canvas">.*?<div class="flex items-start justify-between border border-line-strong rounded p-3 bg-canvas">.*?</div>\n                    </div>', mobile_cards, content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

# quotations.html
with open('quotations.html', 'r') as f:
    content = f.read()

desktop_rows_q = """                        {{> editor-item-desktop name="Design services" tax="None" qty="1" price="450,000.00" amount="450,000.00" }}"""
content = re.sub(r'<tr>.*?Design services.*?</tr>', desktop_rows_q, content, flags=re.DOTALL)

mobile_cards_q = """                    {{> editor-item-mobile name="Design services" tax="None" qty="1" price="450,000.00" amount="450,000.00" }}"""
content = re.sub(r'<div class="flex flex-col border border-line-strong rounded p-3 bg-canvas">.*?</div>\n                    </div>', mobile_cards_q, content, flags=re.DOTALL)

with open('quotations.html', 'w') as f:
    f.write(content)
