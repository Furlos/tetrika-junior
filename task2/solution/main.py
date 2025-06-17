import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import time


def is_russian(text):
    return bool(re.fullmatch(r'[ёЁа-яА-Я\s\-]+', text))


async def process_wikipedia(session, url, counts):
    start = time.time()
    async with session.get(url) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')

    items_count = 0
    for group in soup.find_all('div', class_='mw-category-group'):
        if is_russian(letter := group.h3.text):
            russian_items = [li for li in group.find_all('li') if is_russian(li.text)]
            counts[letter] += len(russian_items)
            items_count += len(russian_items)

    next_page = soup.find('a', string='Следующая страница')
    return next_page['href'] if next_page else None, items_count, time.time() - start


async def main():
    base_url = "https://ru.wikipedia.org"
    url = "/w/index.php?title=Категория:Животные_по_алфавиту&from=А"
    counts = defaultdict(int)

    async with aiohttp.ClientSession() as session:
        page_num = 1
        while url:
            url, cnt, elapsed = await process_wikipedia(session, base_url + url, counts)
            print(f"Страница {page_num}: {cnt} русских названий ({elapsed:.2f} сек)")
            page_num += 1
            if not url: break

    with open('beasts.csv', 'w', encoding='utf-8') as f:
        f.writelines(f"{l},{c}\n" for l, c in sorted(counts.items()))

    print(f"\nИтого: {sum(counts.values())} русских названий")
    print(f"Обработано букв: {len(counts)}")
    print(f"Всего страниц: {page_num - 1}")