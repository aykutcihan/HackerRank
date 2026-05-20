import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    rows = soup.find_all('tr')
    
    grid = {}
    
    for row in rows[1:]:  # skip header
        cols = row.find_all('td')
        if len(cols) == 3:
            try:
                x = int(cols[0].text.strip())
                char = cols[1].text.strip()
                y = int(cols[2].text.strip())
                grid[(x, y)] = char
            except:
                continue
    
    if not grid:
        return
    
    max_x = max(k[0] for k in grid)
    max_y = max(k[1] for k in grid)
    
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            row += grid.get((x, y), ' ')
        print(row)

decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")