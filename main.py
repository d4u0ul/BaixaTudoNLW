#tem que instalar a api via pip
# pip install pytube==10.4.1
import requests
from pytube import YouTube
from bs4 import BeautifulSoup

#url=https://nextlevelweek.com/episodios/reactnative/2/edicao/5
trilhas=["node","elixir","react","reactnative", "flutter"]
qtsAulasJaTeve=2


for x in trilhas:
    urlInicio="https://nextlevelweek.com/episodios/"
    urlTrilha=x
    urlFim = "/edicao/5"
    for i in range(qtsAulasJaTeve):
        urlEps = "/" + str(i+1)
        url=urlInicio+urlTrilha+urlEps+urlFim
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        resultado = soup.find_all('iframe')
        linkYT = (str(resultado[1]))
        print(linkYT[linkYT.rfind("src=\"https://www.youtube.com/embed/") + 5:linkYT.rfind("?autohide")])
        yt = YouTube(linkYT[linkYT.rfind("src=\"https://www.youtube.com/embed/") + 5:linkYT.rfind("?autohide")])
        print(yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download()


