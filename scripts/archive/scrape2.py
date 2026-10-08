import os
import requests
from bs4 import BeautifulSoup
import json

os.makedirs('docs/briefs', exist_ok=True)

session = requests.Session()
url = "https://otuevbo.techmarho.ng/login"
r = session.get(url)
soup = BeautifulSoup(r.text, "html.parser")
token = soup.find("input", {"name": "_token"})["value"]

data = {"_token": token, "email": "ict.swiftypos@gmail.com", "password": "password123"}
r = session.post(url, data=data)
session.get("https://otuevbo.techmarho.ng/admin/users/2/login_as_user")

pages = {
    'employees': 'https://otuevbo.techmarho.ng/user/staffs',
    'attendance': 'https://otuevbo.techmarho.ng/user/attendance',
    'payroll': 'https://otuevbo.techmarho.ng/user/payslips'
}

for name, url in pages.items():
    print("Fetching", name)
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 1. Header Details (Usually in h4 or h1, or breadcrumbs)
    header = soup.find('h4')
    header_text = header.get_text(strip=True) if header else name.title()
    
    # 2. Stats
    stats = []
    for stat in soup.find_all(class_='card-body'):
        text = stat.get_text(separator=' ', strip=True)
        if 'Total' in text or len(text) < 50:
            stats.append(text)
            
    # 3. Actions / Buttons
    buttons = []
    for btn in soup.find_all(['a', 'button']):
        if 'btn' in btn.get('class', []):
            buttons.append(btn.get_text(strip=True))
    buttons = list(set([b for b in buttons if b]))
    
    # 4. Tables
    tables_data = []
    for table in soup.find_all('table'):
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = []
        for tr in table.find_all('tr')[1:4]:
            cols = [td.get_text(strip=True) for td in tr.find_all('td')]
            if cols:
                rows.append(cols)
        tables_data.append({'headers': headers, 'rows': rows})
        
    # 5. Forms
    forms_data = []
    for form in soup.find_all('form'):
        if 'logout' in form.get('action', ''):
            continue
        fields = []
        for inp in form.find_all(['input', 'select', 'textarea']):
            n = inp.get('name')
            t = inp.get('type', 'text') if inp.name == 'input' else inp.name
            if n and n not in ['_token', '_method']:
                fields.append(f"{n} ({t})")
        if fields:
            forms_data.append(fields)
            
    # Write markdown
    md = f"# {header_text}\n\n"
    
    md += "## Layout/Header Details\n"
    md += f"- **Title**: {header_text}\n"
    md += "- **Path**: " + url + "\n\n"
    
    md += "## Stats / Metrics\n"
    if stats:
        for s in set(stats[:4]):
            md += f"- {s}\n"
    else:
        md += "- No stats displayed.\n"
    md += "\n"
    
    md += "## Available Actions/Buttons\n"
    for b in buttons:
        md += f"- {b}\n"
    md += "\n"
    
    md += "## Table Columns\n"
    for t in tables_data:
        md += f"**Columns**: {', '.join(t['headers'])}\n"
        md += "**Example Data**:\n"
        for r in t['rows']:
            md += f"- {', '.join(r)}\n"
        md += "\n"
    
    md += "## Forms\n"
    for idx, f in enumerate(forms_data):
        md += f"**Form {idx+1} Fields**:\n"
        for field in f:
            md += f"- {field}\n"
        md += "\n"
        
    with open(f"docs/briefs/{name}.md", "w") as f:
        f.write(md)
        
print("Done")
