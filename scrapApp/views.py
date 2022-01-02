from django.shortcuts import render, redirect
from .models import *
# Create your views here.
import requests
from bs4 import BeautifulSoup


def scrap(request):
    base_url = 'https://news.ycombinator.com/news?p='
    counter = 1
    total = 1
    while True:
        url = base_url + str(counter)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        contents = soup.find_all('a', class_='storylink')
        c = soup.find_all('td', class_='subtext')
        id = soup.find_all('tr', class_='athing')
        l = contents.__len__()
        for i in range(l):
            print(total)
            index = id[i]['id']
            link = contents[i]['href']
            title = contents[i].contents[0]

            cs = c[i].children
            l = list(cs)
            try:
                a = l[11].contents
                main = a[0].split("\xa0")
                comment = main[0]
            except:
                comment = None
            try:
                Post.objects.create(index=index, title=title,
                                    link=link, comment=comment)
            except:
                pass
            total = total + 1

        more = soup.find_all('a', class_='morelink')
        if more == []:
            break
        counter = counter + 1

    return redirect('home')


# scrap()


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)
