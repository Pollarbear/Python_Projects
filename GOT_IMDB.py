
""" Game of thrones IMDB ratings """
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

#print("test code")

url = 'http://www.imdb.com/title/tt0944947/episodes'
episodes = []
ratings = []
# Go over seasons 1 to 5
for season in range(1, 6):
    r = requests.get(url, params={'season': season})
    #print(r)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    
    listing = soup.find('div', class_="eplist")
    for epnr, div in enumerate(listing.find_all('div', recursive=False)):
        episode = "{}.{}".format(season, epnr + 1)
        rating_el = div.find(class_='ipl-rating-star__rating')
        rating = float(rating_el.get_text(strip=True))
        episodes.append(episode)
        ratings.append(rating)
        print(str(episode) + ' --> '+ str(rating))
episodes = ['S' + e.split('.')[0] if int(e.split('.')[1]) == 1 else '' for e in episodes]
plt.figure()
positions = [a*2 for a in range(len(ratings))]
plt.bar(positions, ratings, align="center", color='b', edgecolor='black', linewidth=1)
plt.xticks(positions, episodes)
plt.xlabel('SEASON/EPISODES', fontsize=12)
plt.ylabel('IMDB_RATING', fontsize=12)
plt.title('Game of Thrones - IMDB',fontsize=20)
plt.show()

