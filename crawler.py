# import facebook_scraper as fs
from facebook_scraper import get_posts, write_posts_to_csv
from datetime import datetime
import json
import csv


class Post:
    def __init__(self, time, text, post_url):
        self.time = time
        self.post_url = post_url
        self.text = text


class PostEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return obj.__dict__  # Convert Post object to a dictionary
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime object to ISO 8601 format
        return super().default(obj)


POST_ID = "592LDS"
cookies = r'D:\Programms\Crawler\FacebookScraper\www.facebook.com_cookies.txt'
options = {"comments": True,
           "allow_extra_requests": False, "posts_per_page": 5}
encoding = 'utf-8'

filename = r'D:\Programms\Crawler\FacebookScraper\output.json'

# region Get posts

# post_list = []
# file_path = r'D:\Programms\Crawler\FacebookScraper\output3.csv'

# output_file = open(filename, 'w', newline='', encoding=encoding)

# for post in get_posts(POST_ID, page_limit=3, cookies=cookies, options=options):
#     if post['text']:
#         keys = list(post.keys())
#         dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore')
#         dict_writer.writeheader()
#         dict_writer.writerow(post)
# p = Post(post['time'], post['text'], post['post_url'])
# post_list.append(p)

# try:
#     with open(file_path, 'w', newline='', encoding=encoding) as file:
#         json.dump(post_list, file, indent=4,
#                   ensure_ascii=False, cls=PostEncoder)
# except IOError as e:
#     print(f"Error writing to file: {e}")

# endregion

# region Write posts to csv

kwargs = {
    "cookies": "D:\Programms\Crawler\FacebookScraper\www.facebook.com_cookies.txt",
}

write_posts_to_csv(**kwargs, filename=filename, pages=300,
                   encoding=encoding, account=POST_ID, matching=".+", format="json")

# endregion
