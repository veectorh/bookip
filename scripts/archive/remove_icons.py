import re

files = ['index.html', 'quotations.html', 'purchases.html']
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove the calendar icon next to date inputs
    content = re.sub(r'<svg class="w-4 h-4 stroke-\[1\.75\] text-muted shrink-0" aria-hidden="true"><use href="#i-calendar"/></svg>\n\s*<input type="date"', '<input type="date"', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
