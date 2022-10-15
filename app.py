from flask import Flask
import os

app = Flask(__name__)

pagefiles = os.listdir()
pages = []

for i in pagefiles:
    if not i.endswith('.html'): continue
    file = open(i)
    content = file.read()
    file.close()
    pages.append(content)
    print(i)
print(pages)

@app.route("/")
def main():
    return pages[0]

@app.route('/home')
def home():
    return pages[0]
