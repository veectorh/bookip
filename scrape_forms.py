import requests
from bs4 import BeautifulSoup

session = requests.Session()
login_url = "https://otuevbo.techmarho.ng/login"
r = session.get(login_url)
soup = BeautifulSoup(r.text, 'html.parser')
token = soup.find('meta', {'name': 'csrf-token'})['content']
session.post(login_url, data={'_token': token, 'email': 'ict.swiftypos@gmail.com', 'password': 'password123'}, allow_redirects=True)
session.get("https://otuevbo.techmarho.ng/admin/users/2/login_as_user", allow_redirects=True)

urls = [
    "https://otuevbo.techmarho.ng/user/customers/create",
    "https://otuevbo.techmarho.ng/user/vendors/create"
]

for url in urls:
    r = session.get(url)
    name = url.split('/')[-2] + '_create'
    with open(f"scraped_pages/{name}.html", 'w') as f:
        f.write(r.text)
    print(f"Scraped {name}")
