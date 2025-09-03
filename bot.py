import os
import automation
from utils import fetch_posts

posts = fetch_posts(page=2,limit = 2)

for number, post in enumerate(posts, start=1):
    automation.launch_notepad()
    automation.make_directory('tjm-project')
    automation.write_post(post)
    automation.save_file(f'post{number}.txt')  