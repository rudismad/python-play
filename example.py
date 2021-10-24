import bs4
import requests
res = requests.get(
    'https://www.cv.lv/lv/search?limit=20&offset=0&categories%5B0%5D=ELECTRONICS_TELECOM&isHourlySalary=false&isRemoteWork=false')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
