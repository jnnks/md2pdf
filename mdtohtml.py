# script to render html from markdown

from grip import render_page
from sys import argv
from os.path import isabs, dirname, exists, splitext, basename, join
from os import mkdir
from shutil import copy
from bs4 import BeautifulSoup

in_file = argv[1]
if not exists(in_file):
    print("Input file does not exist."); print()
    exit()
in_file_name = splitext(basename(in_file))[0]

out_dir = argv[2]
if not exists(out_dir):
    print("Output directory does not exist."); print()
    exit()

print("reading from", in_file)
html = render_page(path=in_file, user_content=True, render_offline=False, render_inline=True, render_wide=True)

# remove unwanted icon
html = BeautifulSoup(html, features="html.parser")
icon = html.find("link", {"rel": "icon"},recursive=True)
icon.replace_with("") 

# remove lots of formatting and decoration
page = html.find("div", {"class": "page"})
content = html.find("div", {"class": "edit-comment-hide"})
page.replace_with(content) 

# copy all images to new render location
images = html.find_all("img")
for img in images:
    path = img["src"]
    if not isabs(path):
        if not exists(join(out_dir, dirname(path))):
            print("mkdir", join(out_dir, dirname(path)))
            mkdir(join(out_dir, dirname(path)))
            
        print("copy image", path, "to", join(out_dir, path))
        copy(path, join(out_dir, path))

out_path = join(out_dir, f"{in_file_name}.html")
print("writing to", out_path)
with open(out_path, "w+") as fp:
    fp.write(str(html))