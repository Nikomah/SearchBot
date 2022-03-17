import requests
from bs4 import BeautifulSoup


def get_content(url):
    header = {
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/96.0.4664.45 Safari/537.36',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
              '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
              }
    resp = requests.get(url, headers=header)
    output = []
    if resp.status_code == 200:
        page = BeautifulSoup(resp.text, 'html.parser')
        tasks = page.find_all('li', class_='content-list__item')
        for item in tasks:
            title = item.find('div', class_='task__title')
            href = title.a['href']
            url = 'https://freelance.habr.com'+href
            text = title.text
            price = item.find('aside', class_='task__column_price').text
            string = f'{url}; {text}; цена: {price}'
            output.append(string)
    # print(*output, sep='\n')
    return output


def parse_content():
    url = 'https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_' \
          'frontend,development_desktop,development_bots,development_scripts,development_other'
    return get_content(url)


if __name__ == '__main__':
    parse_content()
