# import the libraries needed
from urllib import request
import csv
from bs4 import BeautifulSoup

# make a web request to the target URL and parse it with BeautifulSoup
yeah = request.urlopen('https://www.gov.ph/project-list')
bsparsed = BeautifulSoup(yeah.read(), 'html.parser')

# specify the area where the data will be gathered using select method
gov_projects = bsparsed.select('div#projects > div#right-col > ul > li')

# create a csv file and write the data gathered
csv_file = open('gov_projects.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['Project Name','Implementing Agency','Description','Project URL'])
for project in gov_projects:
    writer.writerow([
        project.find('a', {'class': 'name'}).getText(),
        project.find('a', {'class': 'agency'}).getText(),
        project.find('span', {'class': 'description'}).getText(),
        project.find('a', {'class': 'name'})['href']
    ])
csv_file.close()