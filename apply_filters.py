import re

with open('index.html', 'r') as f:
    content = f.read()

content = re.sub(r'<div class="flex flex-col gap-2\.5 mb-2\.5">.*?<button class="shrink-0 text-xs px-2\.5 py-1\.5 rounded-pill border border-line-strong bg-surface text-muted">Paid</button>\n              </div>', '{{> list-mobile-filters }}', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

with open('quotations.html', 'r') as f:
    content = f.read()
    
content = re.sub(r'<div class="flex flex-col gap-2\.5 mb-2\.5">.*?<button class="shrink-0 text-xs px-2\.5 py-1\.5 rounded-pill border border-line-strong bg-surface text-muted">Paid</button>\n              </div>', '{{> list-mobile-filters }}', content, flags=re.DOTALL)

with open('quotations.html', 'w') as f:
    f.write(content)
