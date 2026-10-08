import requests
from bs4 import BeautifulSoup
import json
import os

session = requests.Session()

# Login as admin
login_url = "https://otuevbo.techmarho.ng/login"
r = session.get(login_url)
soup = BeautifulSoup(r.text, 'html.parser')
token = soup.find('meta', {'name': 'csrf-token'})['content']
login_payload = {
    '_token': token,
    'email': 'ict.swiftypos@gmail.com',
    'password': 'password123'
}
session.post(login_url, data=login_payload, allow_redirects=True)

# Login as user 2
login_user_url = "https://otuevbo.techmarho.ng/admin/users/2/login_as_user"
session.get(login_user_url, allow_redirects=True)

urls_to_scrape = [
    "https://otuevbo.techmarho.ng/user/quotations",
    "https://otuevbo.techmarho.ng/user/quotations/create",
    "https://otuevbo.techmarho.ng/user/customers",
    "https://otuevbo.techmarho.ng/user/vendors",
    "https://otuevbo.techmarho.ng/user/purchases",
    "https://otuevbo.techmarho.ng/user/purchases/create"
]

os.makedirs('scraped_pages', exist_ok=True)

for url in urls_to_scrape:
    r = session.get(url)
    name = url.split('/')[-1] if 'create' not in url else url.split('/')[-2] + '_create'
    with open(f"scraped_pages/{name}.html", 'w') as f:
        f.write(r.text)
    print(f"Scraped {name}")

print("Done scraping specific pages.")
