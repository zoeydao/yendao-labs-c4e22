#1. Download webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"

#1.1 Connect to website
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text =  raw_data.decode("utf-8")

#2. Extract ROI (Region of interest)
#2.1 Convert text to soup (cat text thanh html)
soup = BeautifulSoup(webpage_text,"html.parser")

content = soup.find_all("div", "section-content")
list_of_li = content[1].ul.find_all("li")

itunes_chart = []
#getting song's name and artist
for item in list_of_li:
    Title = item.h3.string
    Artist = item.h4.string
    songs = {
        "title": Title,
        "artist": Artist
    }
    itunes_chart.append(songs)

# print(*itunes_chart,sep="\n*****\n")
#Download songs from youtube
from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)

for song in itunes_chart:
    title = song["title"]
    dl.download([title])