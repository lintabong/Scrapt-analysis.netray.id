from URLcrawler import *
from Connection import *
from DateParser import *
from dotenv import load_dotenv
import os

load_dotenv('.env')
 
# create object collection (connection to mongoDB)
collection = connect_to_db(os.getenv('MONGODB_PASS'))

# get target data from .env
cat = os.getenv('CAT').split(',')
# cat = ['membaca-2024']
print('target category: ', cat)

# crawls url-posts from category list ( will take long time / no threading )
urls = url_list(cat)

# list of all url-posts
for i in range(len(urls)):
    print(i, urls[i])

# mongodb repository (collection)
collection = collection.xd

# main function (scrapt every data on a single post)
for i in range(len(urls)):
    data = get_single_post(urls[i])

    post = {
        "date" : date_parser(data[0]),
        "title" : data[1],
        "author" : data[2],
        "post_with_HTML": str(data[3]),
        "post_without_HTML": str(data[4]),
        "tags" : data[5],
        "categories" :data[6],
        "images_link" : data[7]
    }

    inserted_id = collection.insert_one(post).inserted_id

    print(data[0], data[6], data[2])