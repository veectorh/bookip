import re

with open('index.html', 'r') as f:
    content = f.read()

content = re.sub(r'<div class="flex gap-2 mb-2\.5 flex-wrap hidden md:flex">.*?New invoice</button>\n              </div>\n            </div>', '{{> list-desktop-filters new_button_label="New invoice" }}', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

with open('quotations.html', 'r') as f:
    content = f.read()
    
content = re.sub(r'<div class="flex gap-2 mb-2\.5 flex-wrap hidden md:flex">.*?New quotation</button>\n              </div>\n            </div>', '{{> list-desktop-filters new_button_label="New quotation" }}', content, flags=re.DOTALL)

with open('quotations.html', 'w') as f:
    f.write(content)
