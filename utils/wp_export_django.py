#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
from bson import ObjectId
import datetime
import requests
import pymongo
import html2text

MONGO_POOL = pymongo.mongo_client.MongoClient('localhost', 27017)

TBLOG = MONGO_POOL.tblog


API_BASE_URL = 'http://www.ipengtao.com/api/'

def wp2django():
    get_posts_url = API_BASE_URL+'get_posts/'
    resp = requests.get(get_posts_url)
    post = json.loads(resp.content)
    pages = post['pages']

    posts_id = []
    page_list = range(1, pages+1)
    page_list.reverse()
    for page in page_list:
        resp = requests.get(get_posts_url, params={'page': page})
        posts = json.loads(resp.content)['posts']
        for post in posts:
            post_id = post['id']
            posts_id.append(post_id)

    for post_id in posts_id:
        post_url = API_BASE_URL + '/get_post/'
        api_post = json.loads(requests.get(post_url, params={'post_id': post_id}).content)
        post_data = api_post['post']

        title = post_data['title']
        alias_name = post_id
        content = post_data['content']
        h = html2text.HTML2Text()
        h.ignore_links = False
        content = h.handle(content)

        create_date = post_data['date']

        categories, tags = get_categories_and_tags(post_data)
        author = ObjectId("5653ef49b3ce6190342be542")
        data = {
            'title': title,
            'alias_name': str(post_id),
            'content':  content,
            'categories': categories,
            'tags': tags,
            'author': author,
            'created_date': datetime.datetime.strptime(create_date, '%Y-%m-%d %H:%M:%S'),
            'published_dates': []
        }
        TBLOG.article.save(data)
        print u'正在保存%s到数据库' % title




def get_categories_and_tags(post_data):
    categories = post_data['categories']
    tags = post_data['tags']
    category_list = []
    tag_list = []
    for category in categories:
        category_title = category['title']
        category_list.append(category_title)

    for tag in tags:
        tag_title = tag['title']
        tag_list.append(tag_title)

    return category_list, tag_list

if __name__ == '__main__':
    wp2django()
    print 'tranfer complete'
