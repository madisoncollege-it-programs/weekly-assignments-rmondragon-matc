#!/usr/bin/env python3

html_doc = """
 2
 3 <html><head><title>The Dormouse's story</title></head>
 4 <body>
 5 <p class="title"><b>The Dormouse's story</b></p>
 6
 7 <p class="story">Once upon a time there were three little sisters; and there>
 8 <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
 9 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
10 <a href="http://example.com/tillie" class="sister" id="link3">Tillie<a/>;
11 and they lived at the bottom of a well.</p>
12
13 <p class="story">...</p>
14 """


from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())


print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))

