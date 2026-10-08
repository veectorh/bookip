import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()

def login():
    url = "https://otuevbo.techmarho.ng/login"
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    token = soup.find('input', {'name': '_token'})['value']
    
    data = {
        '_token': token,
        'email': 'ict.swiftypos@gmail.com',
        'password': 'password123'
    }
    r = session.post(url, data=data)
    return "dashboard" in r.url or r.status_code == 200

def parse_page(url):
    print(f"Fetching {url}")
    r = session.get(url)
    if r.status_code != 200:
        return f"Failed to fetch {url}, status code {r.status_code}"
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    result = {}
    
    # Check for header/stats
    stats = []
    for stat in soup.find_all(class_='card-body'):
        stats.append(stat.get_text(strip=True))
    result['stats'] = stats
    
    # Look for tables
    tables_data = []
    tables = soup.find_all('table')
    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        
        rows = []
        for tr in table.find_all('tr')[1:]:
            cols = [td.get_text(strip=True) for td in tr.find_all('td')]
            if cols:
                rows.append(cols)
        tables_data.append({'headers': headers, 'sample_rows': rows[:3]})
    result['tables'] = tables_data
    
    # Look for forms/actions
    forms_data = []
    for form in soup.find_all('form'):
        inputs = []
        for inp in form.find_all(['input', 'select', 'textarea']):
            name = inp.get('name')
            if name and name not in ['_token', '_method']:
                inputs.append(name)
        forms_data.append(inputs)
    result['forms'] = forms_data
    
    # Buttons
    buttons = [btn.get_text(strip=True) for btn in soup.find_all(['button', 'a']) if 'btn' in btn.get('class', [])]
    result['buttons'] = list(set(buttons))
    
    return result

if __name__ == "__main__":
    if login():
        print("Logged in successfully.")
        
        pages = {
            'Employees': 'https://otuevbo.techmarho.ng/staffs',  # guessing URL, might need checking
            'Attendance': 'https://otuevbo.techmarho.ng/attendance',
            'Payroll': 'https://otuevbo.techmarho.ng/payroll'
        }
        
        for name, url in pages.items():
            print(f"--- {name} ---")
            data = parse_page(url)
            with open(f"{name.lower()}_data.json", "w") as f:
                json.dump(data, f, indent=2)
            print("Saved", name)
    else:
        print("Login failed.")
