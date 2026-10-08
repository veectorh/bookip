import glob
import re

files = glob.glob('*.html') + glob.glob('src/partials/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # App shell
    content = content.replace('[&[data-layout=mob]]:grid-cols-1', '')
    content = content.replace('grid-cols-[var(--sidebar-width,220px)_1fr]', 'grid-cols-1 md:grid-cols-[var(--sidebar-width,220px)_1fr]')
    
    # Hidden elements
    content = content.replace('hidden [&[data-layout=mob]_&]:block', 'block md:hidden')
    content = content.replace('[&[data-layout=mob]_&]:hidden', 'hidden md:flex')
    # sometimes hidden md:block is better but hidden md:flex works for buttons, let's manually check.
    
    # Grid columns
    content = content.replace('grid-cols-[1fr_280px] [&[data-layout=mob]_&]:grid-cols-1 [&[data-layout=tablet]_&]:grid-cols-1', 'grid-cols-1 lg:grid-cols-[1fr_280px]')
    content = content.replace('grid-cols-2 [&[data-layout=mob]_&]:grid-cols-1', 'grid-cols-1 md:grid-cols-2')

    with open(filepath, 'w') as f:
        f.write(content)
