import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get('https://news.ycombinator.com/news')   # page 1
res2 = requests.get('https://news.ycombinator.com/news?p=2')   # page 2
# print(res.text)
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.select('div')
# print(soup.select('.score'))   # select by class
# print(soup.select('#score_21888096'))    # select by id

links1 = soup1.select('.storylink')    # select by class
links2 = soup2.select('.storylink')    # select by class
# votes = soup.select('.score')   # sometimes, there is no votes
subtexts1 = soup1.select('.subtext')
subtexts2 = soup2.select('.subtext')
# print(links[0], votes[0])

links = links1 + links2
subtexts = subtexts1 + subtexts2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['points'], reverse=True)


def create_custom_hn(links, subtexts):
    hn = []
    for index, item in enumerate(links):
        votes = subtexts[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                title = item.getText()
                href = item.get('href', None)
                hn.append({'title': title, 'link': href, 'points': points})

    return sort_stories_by_votes(hn)


custom_hn = create_custom_hn(links, subtexts)
pprint.pprint(custom_hn, sort_dicts=False)
