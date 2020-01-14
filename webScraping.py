from bs4 import BeautifulSoup
from urllib.request import urlopen
wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url)
wiki_html = wiki_data.read()
wiki_data.close()

page_soup = BeautifulSoup(wiki_html, 'html.parser')
#print (page_soup.encode("utf-8"))
genome_table = page_soup.findAll('table', {'class': 'wikitable sortable'})
#print(genome_table)

genome_table = genome_table[0]
headers = genome_table.findAll('th',{})
#print(headers)

header_titles = []
for header in headers:
    header_titles.append(header.text[:-1])
#print(header_titles)

all_rows = genome_table.findAll('tr',{})
#print(all_rows)

table_data = all_rows[1:]
print(table_data)