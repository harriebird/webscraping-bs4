# import the libraries needed
from urllib import request
import csv
from bs4 import BeautifulSoup

# add headers to prevent the request from being blocked ex. error 403
req_headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive',
}

# make a web request to the target URL and parse it with BeautifulSoup
site_request = request.Request('http://pokemondb.net/pokedex/all', headers=req_headers)
yeah = request.urlopen(site_request)
bsparsed = BeautifulSoup(yeah.read(), 'html.parser')

# specify the area where the data will be gathered using find and select methods
pokemons = bsparsed.find('table',{'id': 'pokedex', 'class':'data-table'}).tbody.select('tr')

# create a csv file and write the data gathered
csv_file = open('pokemons.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['ID','Name','Type','Total','HP','ATK','DEF','SP ATK','SP DEF', 'Speed'])
for pokemon in pokemons:
    writer.writerow([
        pokemon.findAll('td')[0].getText(),
        pokemon.findAll('td')[1].getText(),
        pokemon.findAll('td')[2].getText(),
        pokemon.findAll('td')[3].getText(),
        pokemon.findAll('td')[4].getText(),
        pokemon.findAll('td')[5].getText(),
        pokemon.findAll('td')[6].getText(),
        pokemon.findAll('td')[7].getText(),
        pokemon.findAll('td')[8].getText(),
        pokemon.findAll('td')[9].getText(),
    ])
csv_file.close()