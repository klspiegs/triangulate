try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
import ssl
import requests
from bs4 import BeautifulSoup

file_to_delete = open("result.txt",'w')
file_to_delete.close()
# to search
query = "Pope Francis shocks world, endorses Donald Trump for president"
list = []
for j in search(query, tld="co.in", num=5, stop=5, pause=2):
    list.append(j)
    print(j)

context = ssl._create_unverified_context()
for k in list:
    reqs = requests.get(k)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    title = soup.title
    print(title.string)
    desc = soup.find("meta", property="og:description")
    print(desc["content"] if desc else "No meta desc given")
    with open('result.txt', 'a') as f:
      f.write(title.string.upper())
      f.write('\n')
      f.write(desc["content"] if desc else "No meta desc given")
      f.write('\n')
      f.write(k)
      f.write('\n')
      f.write('\n')

