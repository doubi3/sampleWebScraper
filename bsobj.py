import requests
from bs4 import Beautifulsoup

sample_obj = []


# This writes a new file with the sample_obj content
with open('index.html', 'w') as f:
    f.write(sample_obj)
    
soup = Beautifulsoup(sample_obj)


# Pretty can render a cleaner code, e.g. *.html
#print(soup.prettify())

# Tag
soup.b # This will print the first <b> tag in a html file
soup.p # Does the same with the <p> tag
print#will find the <b> tags(soup.find('b'))
print#will finds all <b> tags(soup.find_all('b'))
print#will find the name of the <b> tags(soup.b.name)

#changing tag names
#tag = soup.b
#tag.name = "blockquote"

#print(tag['id'])
#print(tag['any_attribute'])

#print(tag.attrs) # returns a dictionary of the attributes
#del tag['id']