import json
from bs4 import BeautifulSoup
from constants import WORK_PATH


html_path = list(WORK_PATH.glob('*.html'))[0]
with open(html_path) as html_file:
    main = BeautifulSoup(html_file, 'html5lib').main

info = dict()
header = main.header

info['name'] = main.header.h1.string
info['author'] = main.header.find('h2', class_='main').a.string

description, detail, content = main.find_all('section')

info['description'] = description.find('div', class_='content').p.string

date, learning_paths, topics = detail.find_all('div', class_='group')

info['date'] = date.div.string

info['learning_paths'] = [a.string for a in learning_paths.ul.find_all('a')]
info['topics'] = [a.string for a in topics.ul.find_all('a')]

info['resources'] = [a['href'] for a in detail.find('div', class_='bottom').ul.find_all('a')]

content = content.div
info['sections'] = []
section_name = content.find('div')
print(section_name)

while section_name:
    info_section = dict()
    info_section['name'] = section_name.h3.string
    info_section['items'] = []

    section_list = section_name.next_sibling.next_sibling

    for item in section_list.find_all('div', class_='text'):
        info_item = dict()
        info_item['title'] = item.h3.a.string
        info_item['time'] = item.find('a', class_='timestamp').span.string
        info_item['description'] = item.find('div', class_='description').string

        info_section['items'].append(info_item)


    info['sections'].append(info_section)

    section_name = section_list.next_sibling.next_sibling


print(json.dumps(info, indent=4))

json_file = WORK_PATH.joinpath('info.json').open('w')
json.dump(info, json_file, indent=4)
