from bs4 import BeautifulSoup
import urllib.request
import re

# URL for stackoverflow...
url = 'https://stackoverflow.com/'

# This requests the web page of stackoverflow from where questions are scraped
webpage = urllib.request.urlopen(url)

# Using the BeautifulSoup library we parse the html webpage
soup = BeautifulSoup(webpage, 'html.parser')

# Each question on stackoverflow is associated with <a href tag>...which is a link
# Since all questions are on the url/questions/some question id...we ues a regular expression
# to find all questions.Also all questions in the class : question-hyperlink
# All the questions are extracted using findAll() and get_text()function
for question in soup.findAll('a', attrs={'href': re.compile("^/questions/[0-9]"), 'class': "question-hyperlink"}):
    print(question.get_text())
