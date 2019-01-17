# from django.shortcuts import render
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Contact_usForm

# from datetime import timedelta, timezone, datetime
# from photograaf.models import Headline, UserProfile

# Create your views here.

def scrapezzp():
    # user_p = UserProfile.objects.filter(user=request.user).first()
    # user_p.last_scape = datetime.now(timezone.utc)
    # user_p.save()

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116"}
    url = 'https://www.imk.nl/nieuws/'
    page = session.get(url, verify=False)

    soup = BeautifulSoup(page.content, 'html.parser')

    posts = soup.find_all('div',{'class':'blog-entry-inner'})
    for i in posts:
        link = i.find_all('a',{'rel': 'bookmark'})[1]['href']
        title = i.find_all('a',{'rel': 'bookmark'})[1].text[0:50]
        image_source = i.find('img',{'width':'680'})['src']
        date = i.find('span', {'class': 'updated'}).text
        summary = i.find('div', {'class': 'blog-entry-excerpt'}).text[0:80]
        loop_times = range(1, 3)

        # blogs = {'link': link, 'title': title, 'image_source': image_source, 'summary': summary, 'date': date}
        blogs = {'image_source': image_source, 'date': date, 'title': title, 'summary': summary, 'link': link}

        return  blogs

def scrapepic():
    # user_p = UserProfile.objects.filter(user=request.user).first()
    # user_p.last_scape = datetime.now(timezone.utc)
    # user_p.save()

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116"}
    url = 'https://www.pf.nl'
    page = session.get(url, verify=False)

    soup = BeautifulSoup(page.content, 'html.parser')

    posts = soup.find_all('div',{'id':'main-content-inner'})
    for i in posts:
        link = i.find_all('a',{'rel': 'category'})[1]['href']
        title = i.find_all('a',{'rel': 'bookmark'})[1].text[0:50]
        image_source = i.find('img',{'class':'attachment-thumbnail'})['src']
        date = i.find('time', {'class': 'entry-date'}).text
        summary = i.find('div', {'class': 'entry-summary'}).text[0:80]
        loop_times = range(1, 3)

        blogspic = {'link': link, 'title': title, 'image_source': image_source, 'summary': summary, 'date': date}
        return blogspic

def scrapemark():
    # user_p = UserProfile.objects.filter(user=request.user).first()
    # user_p.last_scape = datetime.now(timezone.utc)
    # user_p.save()

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.116"}
    url = 'https://www.scientias.nl'
    page = session.get(url, verify=False)

    soup = BeautifulSoup(page.content, 'html.parser')

    posts = soup.find_all('main',{'id':'main'})
    for i in posts:
        link = i.find_all('a')[1]['href']
        title = i.find_all('h2',{'class': 'post-title'})[0].text[0:50]
        image_source = i.find('img',{'class':'attachment-barcelona-md'})['src']
        date = i.find('li', {'class': 'post-date'}).text
        summary = i.find('p', {'class': 'post-excerpt'}).text[0:80]
        loop_times = range(1, 3)

        blogsmark = {'link': link, 'title': title, 'image_source': image_source, 'summary': summary, 'date': date}
        return blogsmark


def home(request):
    blogs = scrapezzp()
    blogspic = scrapepic()
    blogmark = scrapemark()
    form = Contact_usForm()
    if request.method =='POST':
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'photograaf/index.html', {'blogs': blogs, "blogspic": blogspic, "blogmark": blogmark, 'form': form })

def contact_view(request):
    if request.method =='POST':
        form = Contact_usForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
    return render(request, 'photograaf/index.html', {})
