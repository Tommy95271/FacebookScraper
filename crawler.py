"""
Download comments for a public Facebook post.
"""

# import facebook_scraper as fs
from facebook_scraper import get_posts
from bs4 import BeautifulSoup as soup
import requests

POST_ID = "592LDS"
cookies='D:\Programms\Crawler\FacebookScraper\www.facebook.com_cookies.txt'

options = {"comments": True, "allow_extra_requests": False, "posts_per_page": 5}

post_list = []

for post in get_posts(POST_ID, page_limit=3, cookies=cookies, options=options):
    if post['text'] and '沒看到，請用搜尋股市小黑' not in post['text']:
        # ttt = post['text']
        # source = requests.get(post['post_url'])
        # html = requests.get(post['post_url']).text
        # html = soup(html, 'html.parser')
        # text_of_post = html.find('title').get_text()
        post_list.append(str(post['time']) + '\r\n' + str(post['text']))
        post_list.append('------------------------------------------------------')
        #post_list.append(text_of_post)
        #post_list.append('------------------------------------------------------')
        post_list.append(str(post['post_url']))
    
post_data = '\n'.join(post_list)
    
file_path = r'D:\\Programms\\Crawler\\FacebookScraper\\output.txt'
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(post_data)
except IOError as e:
    print(f"Error writing to file: {e}")

# extract the comments part
# comments = post['comments_full']

# process comments as you want...
# for comment in comments:

    # e.g. ...print them
#     print(comment)

    # e.g. ...get the replies for them
#     for reply in comment['replies']:
#         print(' ', reply)