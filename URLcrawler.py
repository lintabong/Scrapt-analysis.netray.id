import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv('.env')


# create list data of urls
def url_list(_listCategory):
    url = []
    counterPost = 0
    for i in range(len(_listCategory)):
        req = requests.get(os.getenv('CATEGORYTARGET') + _listCategory[i] + '/page/1')


        # find total pages of a single category
        content = BeautifulSoup(req.content, 'html.parser')
        pages = content.find('span', class_ = 'pages')
        

        # get max pages/posts from a known category
        max_page = int(pages.text.replace('Halaman 1 dari ','')) + 1
        

        # crawl link from title of a post
        counterPerCat = 0
        for j in range(1, max_page):
            req = requests.get(os.getenv('CATEGORYTARGET') + _listCategory[i] + '/page/' + str(j))

            content = BeautifulSoup(req.content, 'html.parser')

            title = content.find_all('h3', class_='entry-title td-module-title')

            for k in range(len(title)):
                url.append(title[k].find('a').get('href'))
                counterPerCat += 1
                counterPost += 1

                print('cat:', _listCategory[i], ', page:', counterPerCat, ', pages found:', counterPost, ', title:', title[k].text.strip())


    return url


# get all data from every single post
def get_single_post(_url):
    req = requests.get(_url)
    body = BeautifulSoup(req.content, 'html.parser')


    # find published date
    published_date = body.find('time', class_='entry-date')


    # find title of a post
    try:
        title = body.find('h2')
    except:
        title = ''


    # find author 
    author = body.find('a', class_='tdb-author-name')


    # get resources inside body post 
    postWithHTML = body.find_all('div', class_='tdb-block-inner td-fix-index')

    postWithoutHTML = ''
    for paragraph in postWithHTML:
        for paragraphWihtoutHTML in paragraph.find_all('p'):
            postWithoutHTML = postWithoutHTML + paragraphWihtoutHTML.text


    # get tags from a body post
    tags = []
    try:
        tag = body.find('ul', class_='tdb-tags')
        tag = tag.find_all('a')
        for i in range(len(tag)):
            tags.append(tag[i].text.strip())
    except:
        tags = []


    # get categories from a body post
    categories = []
    try:
        cat = body.find_all('a', class_='tdb-entry-category')
        for i in range(len(cat)):
            categories.append(cat[i].text.strip())
    except:
        categories = []


    # get images from a boty post
    images = []
    img = body.select('img')
    for i in range(len(img)):
        images.append(img[i].get('src'))

    
    return published_date.text, title.text, author.text, postWithHTML, postWithoutHTML, tags, categories, images